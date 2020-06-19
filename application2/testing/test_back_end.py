import requests
import unittest

from flask import url_for
from flask_testing import TestCase

from application import app


class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        return app


class TestViews(TestBase):

    def test_animalpage_view(self):
        """
        Test that animalpage is accessible.
        """
        response = self.client.get(url_for('animal_name'))
        self.assertEqual(response.status_code, 200)


    def test_noisepage_view(self):
        """
        Test that the noise page is accessible.
        """
        response = self.client.post(url_for('animal_noise'))
        self.assertEqual(response.status_code, 200)

    def test_noisepage_cat(self):
        """
        Test that when cat is sent we get the result of meow.
        """
        response = self.client.post(url_for('animal_noise'), data="cat")
        self.assertIn(b'meow', response.data)

    def test_noisepage_dog(self):
        """
        Test that when dog is sent we get the result of woof.
        """
        response = self.client.post(url_for('animal_noise'), data="dog")
        self.assertIn(b'woof', response.data)

    def test_noisepage_cow(self):
        """
        Test that when cow is sent we get the result of moo.
        """
        response = self.client.post(url_for('animal_noise'), data="cow")
        self.assertIn(b'moo', response.data)