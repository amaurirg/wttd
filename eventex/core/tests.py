from django.test import TestCase


class HomeTest(TestCase):
    """GET / must return status code 200"""
    def setUp(self):
        self.response = self.client.get('/')


    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

