#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase

from django_dandelion.exceptions import DandelionException
from django_dandelion.datatxt import EntityExtraction, TextSimilarity, TextClassification, LanguageDetection, \
    SentimentAnalysis


class TestDataTXT(TestCase):
    def test_nex(self):
        datatxt = EntityExtraction()
        datatxt.params = 'text', 'They say Apple is better than Windows'
        datatxt.params = 'lang', 'en'
        datatxt.params = 'min_confidence', 0.6
        datatxt.params = 'min_length', 2
        datatxt.params = 'social.hashtag', False
        datatxt.params = 'social.mention', False
        datatxt.params = 'include', ''
        datatxt.params = 'extra_types', ''
        datatxt.params = 'country', ''
        datatxt.params = 'custom_spots', ''
        results = datatxt.analyze()
        datatxt.analyze()  # cache

        self.assertEqual(
            {annotation.uri for annotation in results.annotations},
            {'http://en.wikipedia.org/wiki/Apple_Inc.', 'http://en.wikipedia.org/wiki/Microsoft_Windows'}
        )
        with self.assertRaises(DandelionException):
            datatxt.params = 'lang', 'eng'
            datatxt.analyze()

    def test_sim(self):
        datatxt = TextSimilarity()
        datatxt.params = 'text1', 'Reports that the NSA eavesdropped on world leaders have "severely' \
                                  ' shaken" relations between Europe and the U.S., German Chancellor' \
                                  ' Angela Merkel said.'
        datatxt.params = 'text2', 'Germany and France are to seek talks with the US to settle a row ' \
                                  'over spying, as espionage claims continue to overshadow an EU ' \
                                  'summit in Brussels.'
        datatxt.params = 'lang', 'en'
        datatxt.params = 'bow', 'never'
        datatxt.params = 'nex.min_confidence', 0.6
        datatxt.params = 'nex.min_length', 2
        datatxt.params = 'nex.social.hashtag', False
        datatxt.params = 'nex.social.mention', False
        datatxt.params = 'nex.include', ''
        datatxt.params = 'nex.extra_types', ''
        datatxt.params = 'nex.country', ''
        datatxt.params = 'nex.custom_spots', ''
        results = datatxt.analyze()
        datatxt.analyze()  # cache
        self.assertGreater(results.similarity, 0.5)
        with self.assertRaises(DandelionException):
            datatxt.params = 'lang', 'eng'
            datatxt.analyze()

    def test_cl(self):
        datatxt = TextClassification()
        classifier = datatxt.UserDefinedClassifiers()
        classifier.list()
        obj = classifier.create(data=u'{"description": "My first model for classifying news","lang": "en",'
                                     u'"categories": [{"name": "Sport","topics": '
                                     u'{"http://en.wikipedia.org/wiki/Sport": 2.0,'
                                     u'"http://en.wikipedia.org/wiki/Baseball": 1.0,'
                                     u'"http://en.wikipedia.org/wiki/Basketball": 1.0,'
                                     u'"http://en.wikipedia.org/wiki/Football": 1.0}},'
                                     u'{"name": "Politics","topics": {"Politics": 2.0,"Politician": 1.5,'
                                     u'"David Cameron": 1.0,"Angela Merkel": 1.0}}]}')
        obj = classifier.update(data=u'{"description": "My first model for classifying news","lang": "en",'
                                     u'"categories": [{"name": "Sport","topics": '
                                     u'{"http://en.wikipedia.org/wiki/Sport": 2.0,'
                                     u'"http://en.wikipedia.org/wiki/Baseball": 1.0,'
                                     u'"http://en.wikipedia.org/wiki/Basketball": 1.0,'
                                     u'"http://en.wikipedia.org/wiki/Football": 1.0}},'
                                     u'{"name": "Politics","topics": {"Politics": 2.0,"Politician": 1.5,'
                                     u'"David Cameron": 1.0,"Angela Merkel": 1.0}}]}',
                                id=obj.id)
        obj = classifier.read(id=obj.id)
        datatxt.params = 'text', 'See how the main parties are doing in the latest opinion polls on voting intention'
        datatxt.params = 'model', obj.id
        results = datatxt.analyze()
        datatxt.analyze()  # cache
        classifier.delete(id=obj.id)

        self.assertEqual(results.categories[0].name, 'Politics')
        self.assertGreater(results.categories[0].score, 0.3)
        with self.assertRaises(DandelionException):
            datatxt.params = 'model', False
            datatxt.analyze()

    def test_li(self):
        datatxt = LanguageDetection()
        datatxt.params = 'text', 'Le nostre tre M sono: mafia, mamma, mandolino'
        results = datatxt.analyze()
        datatxt.analyze()  # cache

        self.assertEqual([entry.lang for entry in results.detectedLangs], ['it'])
        self.assertGreater(results.detectedLangs[0].confidence, 0.9999)

    def test_sent(self):
        datatxt = SentimentAnalysis()
        datatxt.params = 'text', 'Grande applicazione, grande social! Viva Twitter'
        datatxt.params = 'lang', 'en'
        results = datatxt.analyze()
        datatxt.analyze()  # cache

        self.assertEqual(results.sentiment.type, 'positive')
        self.assertGreater(results.sentiment.score, 0.5)
        with self.assertRaises(DandelionException):
            datatxt.params = 'lang', 'eng'
            datatxt.analyze()
