from django.test import TestCase

from eventex.core.managers import PeriodManager
from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(title='Título da Palestra')

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many speakers and vice-versa"""
        self.talk.speakers.create(
            name='Amauri Rossetti',
            slug='amauri-rossetti',
            website='http://amaurirg.github.io/'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_verbose_name_Talk(self):
        self.assertEqual('palestra', Talk._meta.verbose_name)

    def test_verbose_name_plural_Talk(self):
        self.assertEqual('palestras', Talk._meta.verbose_name_plural)

    def test_verbose_name_fields(self):
        contents = (
            ('título', 'title'),
            ('início', 'start'),
            ('descrição', 'description'),
            ('palestrantes', 'speakers'),
        )
        for name, field in contents:
            with self.subTest():
                self.assertEqual(name, Talk._meta.get_field(field).verbose_name)

    def test_str(self):
        self.assertEqual('Título da Palestra', str(self.talk))

    def test_title_blank(self):
        field = Talk._meta.get_field('title')
        self.assertFalse(field.blank)

    def test_fields_blank(self):
        fields = [
            'start',
            'description',
            'speakers',
        ]
        for field in fields:
            with self.subTest():
                self.assertTrue(Talk._meta.get_field(field).blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start='11:59')
        Talk.objects.create(title='Afternoon Talk', start='12:00')

    def test_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)

    def test_at_morning(self):
        qs = Talk.objects.at_morning()
        expected = ['Morning Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)

    def test_at_afternoon(self):
        qs = Talk.objects.at_afternoon()
        expected = ['Afternoon Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)
