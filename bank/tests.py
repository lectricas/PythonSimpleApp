from django.test import TestCase
from django.urls import reverse

from django.test import Client


class AccountTests(TestCase):

    def test_create_account(self):
        c = Client()
        c.post(
            reverse('bank:create_account'),
            '{"currency": "RUB", "name": "qwer"}',
            content_type="application/json"
        )
