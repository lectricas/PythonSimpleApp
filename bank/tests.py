"""Module docstring"""

from django.test import TestCase
from django.urls import reverse
from django.test import Client

from bank.models import Account


class AccountBasicTests(TestCase):
    """Class docstring"""

    def test_create_account_ok(self):
        """Simple create test OK"""
        client = Client()
        response = client.post(
            reverse('bank:create_account'),
            '{"currency": "RUB", "name": "qwer"}',
            content_type="application/json"
        )
        self.assertContains(response, 'Ok')

    def test_create_account_error(self):
        """Simple create test ERROR"""
        account = Account(pk=1, currency="RUB", name="1")
        account.save()
        client = Client()
        response = client.post(
            reverse('bank:create_account'),
            '{"currency": "RUB", "name": "1"}',
            content_type="application/json"
        )
        self.assertContains(response, 'Error')

    def test_delete_account_ok(self):
        """Simple delete test OK"""
        account = Account(pk=1, currency="RUB", name="1")
        account.save()
        client = Client()
        response = client.post(
            reverse('bank:delete_account'),
            '{"account_id": "1"}',
            content_type="application/json"
        )
        self.assertContains(response, 'Ok')

    def test_delete_account_error(self):
        """Simple delete test ERROR"""
        client = Client()
        response = client.post(
            reverse('bank:delete_account'),
            '{"account_id": "1"}',
            content_type="application/json"
        )
        self.assertContains(response, 'Error')


class AccountIntegrationTests(TestCase):
    """Simple class docstring"""

    def test_create_delete_account(self):
        """Multiple delete test OK"""
        client = Client()
        client.post(
            reverse('bank:create_account'),
            '{"currency": "RUB", "name": "qwer"}',
            content_type="application/json"
        )

        response = client.post(
            reverse('bank:delete_account'),
            '{"account_id": "1"}',
            content_type="application/json"
        )
        self.assertContains(response, 'Ok')

    def test_create_delete_delete_account(self):
        """Multiple delete test ERROR"""
        client = Client()
        client.post(
            reverse('bank:create_account'),
            '{"currency": "RUB", "name": "qwer"}',
            content_type="application/json"
        )

        client.post(
            reverse('bank:delete_account'),
            '{"account_id": "1"}',
            content_type="application/json"
        )

        response = client.post(
            reverse('bank:delete_account'),
            '{"account_id": "1"}',
            content_type="application/json"
        )

        self.assertContains(response, 'Error')
