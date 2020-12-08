from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Amauri Rossetti',
            slug='amauri-rossetti',
            photo='../static/img/amauri.jpg'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='amauri@gmail.com',
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='11-99999-8888',
        )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_verbose_name_Contact(self):
        self.assertEqual('contato', Contact()._meta.verbose_name)

    def test_verbose_name_plural_Contact(self):
        self.assertEqual('contatos', Contact()._meta.verbose_name_plural)

    def test_verbose_name_speaker(self):
        self.assertEqual('palestrante', Contact._meta.get_field('speaker').verbose_name)

    def test_verbose_name_kind(self):
        self.assertEqual('tipo', Contact._meta.get_field('kind').verbose_name)

    def test_verbose_name_value(self):
        self.assertEqual('contato', Contact._meta.get_field('value').verbose_name)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='amauri@gmail.com',
        )
        self.assertEqual('amauri@gmail.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Amauri Rossetti',
            slug='amauri-rossetti',
            photo='../static/img/amauri.jpg',
        )

        s.contact_set.create(kind=Contact.EMAIL, value='amauri@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='11-99999-8888')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['amauri@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['11-99999-8888']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
