from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = {
            'name': 'Amauri',
            'cpf': '12345678901',
            'email': 'contato@eventex.com.br',
            'phone': '11-99999-8888'
        }
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expected = 'Confirmação de inscrição'
        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        expected = 'contato@eventex.com.br'
        self.assertEqual(expected, self.email.from_email)

    def test_subscription_email_to(self):
        expected = ['contato@eventex.com.br' ]
        self.assertEqual(expected, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Amauri',
            '12345678901',
            'contato@eventex.com.br',
            '11-99999-8888'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
