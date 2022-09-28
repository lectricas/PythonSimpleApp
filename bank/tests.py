from django.test import TestCase
from django.urls import reverse
from django.test import Client

from bank.models import Account


class AccountBasicTests(TestCase):

    def test_create_account_ok(self):
        c = Client()
        response = c.post(
            reverse('bank:create_account'),
            '{"currency": "RUB", "name": "qwer"}',
            content_type="application/json"
        )
        self.assertContains(response, 'Ok')

    def test_create_account_error(self):
        account = Account(pk=1, currency="RUB", name="1")
        account.save()
        c = Client()
        response = c.post(
            reverse('bank:create_account'),
            '{"currency": "RUB", "name": "1"}',
            content_type="application/json"
        )
        self.assertContains(response, 'Error')

    def test_delete_account_ok(self):
        account = Account(pk=1, currency="RUB", name="1")
        account.save()
        c = Client()
        response = c.post(
            reverse('bank:delete_account'),
            '{"account_id": "1"}',
            content_type="application/json"
        )
        self.assertContains(response, 'Ok')

    def test_delete_account_error(self):
        c = Client()
        response = c.post(
            reverse('bank:delete_account'),
            '{"account_id": "1"}',
            content_type="application/json"
        )
        self.assertContains(response, 'Error')


class AccountIntegrationTests(TestCase):

    def test_create_delete_account(self):
        c = Client()
        c.post(
            reverse('bank:create_account'),
            '{"currency": "RUB", "name": "qwer"}',
            content_type="application/json"
        )

        response = c.post(
            reverse('bank:delete_account'),
            '{"account_id": "1"}',
            content_type="application/json"
        )
        self.assertContains(response, 'Ok')

    def test_create_delete_delete_account(self):
        c = Client()
        c.post(
            reverse('bank:create_account'),
            '{"currency": "RUB", "name": "qwer"}',
            content_type="application/json"
        )

        c.post(
            reverse('bank:delete_account'),
            '{"account_id": "1"}',
            content_type="application/json"
        )

        response = c.post(
            reverse('bank:delete_account'),
            '{"account_id": "1"}',
            content_type="application/json"
        )

        self.assertContains(response, 'Error')
