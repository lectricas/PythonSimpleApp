"""Module docstring"""

import pytest
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from bank.models import Account
from bank_proto.bank_pb2 import DepositMessage


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


@pytest.fixture(scope='module')
def grpc_add_to_server():
    from bank_proto.bank_pb2_grpc import add_BankServiceServicer_to_server
    return add_BankServiceServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    from bank.services import BankService

    return BankService()


@pytest.fixture(scope='module')
def grpc_stub_cls(grpc_channel):
    from bank_proto.bank_pb2_grpc import BankServiceStub
    return BankServiceStub


@pytest.mark.django_db(transaction=True)
def testDepositMessage(grpc_stub):
    """Пока только один тест, и плохой, не успеваю. Постараюсь добавить параметризацию попозже"""
    obj = Account.objects.create(name="Hello", currency="RUB")
    obj.save()
    obj.refresh_from_db()
    request = DepositMessage(account_id=1, amount=200, currency="RUB")
    response = grpc_stub.Deposit(request)
    assert response.code == 1
    assert response.message == "Added"
