from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url
from django.test import TestCase


class TestSpaces(TestCase):
    def test_index(self):
        response = self.client.get(resolve_url('spaces:index'))
        self.assertEqual(response.status_code, 200)

