from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    """GET / must return status code 200"""
    def setUp(self):
        self.response = self.client.get(r('home'))


    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        self.assertContains(self.response, f'''href="{r('subscriptions:new')}"''')

    def test_speakers(self):
        """Must show keynote speakers"""
        contents = [
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'Alan Turing',
            'http://hbn.link/turing-pic'
        ]
        for content in contents:
            with self.subTest():
                self.assertContains(self.response, content)

    def test_speakers_link(self):
        expected = f'''href="{r('home')}#speakers"'''
        self.assertContains(self.response, expected)

