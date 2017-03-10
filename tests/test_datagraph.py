#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase

from django_dandelion.exceptions import DandelionException
from django_dandelion.datagraph import Wikisearch


class TestDatagraph(TestCase):
    def test_wikisearch(self):
        datagraph = Wikisearch()
        datagraph.params = 'text', 'Duomo di Trento'
        datagraph.params = 'lang', 'it'
        datagraph.params = 'limit', 5
        results = datagraph.analyze()
        datagraph.analyze()  # cache

        self.assertEqual(results.entities[0].title, "Cattedrale di San Vigilio")
        with self.assertRaises(DandelionException):
            datagraph.params = 'lang', 'eng'
            datagraph.analyze()
