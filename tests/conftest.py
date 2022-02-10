import os

import pytest
from dotenv import load_dotenv

from crypto_pay_api.api import CryptoPay


@pytest.fixture(name="api")
def get_api():
    load_dotenv()
    api = CryptoPay(token=os.getenv("token"))
    api.client.base_url = "https://testnet-pay.crypt.bot/api/"
    return api
