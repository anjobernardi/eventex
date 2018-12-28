from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Andre Bernardi", cpf='12345678901',
                    email='andre.bernardi@fm.usp.br', phone='11-95343-5443')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com', 'andre.bernardi@fm.usp.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Andre Bernardi',
            '12345678901',
            'andre.bernardi@fm.usp.br',
            '11-95343-5443',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
