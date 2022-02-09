import os

from crypto_pay_api.api import CryptoPay
from crypto_pay_api.enums import Asset, Button

api = CryptoPay(token=os.getenv("token"))


def test_get_invoices():
    api.get_invoices()


def test_get_me():
    api.get_me()


def test_get_balance():
    api.get_balance()


def test_get_currencies():
    api.get_currencies()


def test_get_exchange_rates():
    api.get_exchange_rates()


def test_create_invoice():
    api.create_invoice(
        asset=Asset.TON.value,
        amount='1',
        description='test',
        paid_btn_name=Button.VIEW_ITEM.value,
        paid_btn_url='https://test.com'
    )


# def test_transfer():
#     api.transfer(user_id='@tososomaru', asset=Asset.TON.value, amount='1', spend_id=binascii.hexlify(os.urandom(20)))
