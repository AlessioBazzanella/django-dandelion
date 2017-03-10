#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase

from django_dandelion.base import AttributeDict
from django_dandelion.datatxt import EntityExtraction
from django_dandelion.exceptions import DandelionException


class TestAttributeDict(TestCase):
    def setUp(self):
        self.dict = AttributeDict()

    def test_all(self):
        self.dict.name = 'foo'
        self.assertEqual(self.dict.name, 'foo')

        del self.dict.name
        with self.assertRaises(KeyError):
            print(self.dict.name)


class TestCommon(TestCase):
    def test_init_params(self):
        EntityExtraction(text='They say Apple is better than Windows')

    def test_key_error(self):
        datatxt = EntityExtraction()
        with self.assertRaises(DandelionException):
            datatxt.params = 'key', 'value'

    def test_key_unique_substitution(self):
        datatxt = EntityExtraction()
        datatxt.params = 'text', 'They say Apple is better than Windows'
        datatxt.params = 'url', 'http://www.google.com'

    def test_get_params(self):
        datatxt = EntityExtraction()
        self.assertEqual(datatxt.params, {})

    def test_set_params_error(self):
        datatxt = EntityExtraction()
        with self.assertRaises(DandelionException):
            datatxt.params = 'one', 'two', 'three'

    def test_delete_params(self):
        datatxt = EntityExtraction()
        del datatxt.params
