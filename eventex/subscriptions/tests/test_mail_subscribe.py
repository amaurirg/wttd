from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = {
            'name': 'Amauri',
            'cpf': '12345678901',
            'email': 'amauritestdev@gmail.com',
            'phone': '11-99999-8888'
        }
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expected = 'Confirmação de inscrição'
        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        expected = 'amauritestdev@gmail.com'
        self.assertEqual(expected, self.email.from_email)

    def test_subscription_email_to(self):
        expected = ['amauritestdev@gmail.com' ]
        self.assertEqual(expected, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Amauri',
            '12345678901',
            'amauritestdev@gmail.com',
            '11-99999-8888'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)