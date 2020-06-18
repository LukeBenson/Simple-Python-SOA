import unittest
import requests

from flask import url_for
from flask_testing import TestCase

from application import app


class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
    def tearDown(self):
        """
        Will be called after every test
        """


class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_animalpage_view(self):
        """
        Test that the animal page is accessible without login
        """
        response = self.client.get(url_for('animal'))
        self.assertEqual(response.status_code, 200)