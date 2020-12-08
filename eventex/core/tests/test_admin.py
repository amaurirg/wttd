from django.contrib.admin import ModelAdmin
from django.test import TestCase
from eventex.core.models import Contact, Talk
from eventex.core.admin import ContactInLine


class ContactInLineAdminTest(TestCase):
    def test_ContactInLine_fields(self):
        contents = (
            (Contact, ContactInLine.model),
            (1, ContactInLine.extra)
        )
        for expected, field in contents:
            with self.subTest():
                self.assertEqual(expected, field)
