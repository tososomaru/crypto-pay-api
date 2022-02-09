from typing import Optional, List
from dacite import from_dict

from .client import ApiClient
from .enums import Button, Asset, Status
from .items import Invoice, Transfer
from .config import app_config


class CryptoPay:
    base_url = app_config.base_url

    def __init__(self, token, client=None):
        self.client = client or ApiClient(
            base_url=self.base_url, token=token
        )

    def get_me(self):
        """
        Use this method to test your app's authentication token. Requires no parameters.
        On success, returns basic information about an app.

        :return:
        """
        return self.client.get("getMe")

    def create_invoice(
        self,
        asset: Asset,
        amount: str,
        description: Optional[str] = None,
        hidden_message: Optional[str] = None,
        paid_btn_name: Optional[Button] = None,
        paid_btn_url: Optional[str] = None,
        payload: Optional[str] = None,
        allow_comments: Optional[bool] = None,
        allow_anonymous: Optional[bool] = None,
        expires_in: Optional[int] = None,
    ) -> Invoice:
        """
        Use this method to create a new invoice. On success, returns an object of the created invoice.

        :param asset: Currency code. Supported assets: “BTC”, “TON”, “ETH” (testnet only), “USDT”, “USDC” and “BUSD”.
        :param amount: Amount of the invoice in float. For example: 125.50
        :param description:  Description for the invoice. User will see this description when they pay the invoice. Up to 1024 characters.
        :param hidden_message: Text of the message that will be shown to a user after the invoice is paid. Up to 2o48 characters.
        :param paid_btn_name: Name of the button that will be shown to a user after the invoice is paid.
        :param paid_btn_url: Required if paid_btn_name is used. URL to be opened when the button is pressed. You can set any success link (for example, a link to your bot). Starts with https or http.
        :param payload: Any data you want to attach to the invoice (for example, user ID, payment ID, ect). Up to 4kb.
        :param allow_comments: Allow a user to add a comment to the payment. Default is true.
        :param allow_anonymous: Allow a user to pay the invoice anonymously. Default is true.
        :param expires_in: You can set a payment time limit for the invoice in seconds. Values between 1-2678400 are accepted.

        """

        response = self.client.get(
            "createInvoice",
            asset=asset,
            amount=amount,
            description=description,
            hidden_message=hidden_message,
            paid_btn_name=paid_btn_name,
            paid_btn_url=paid_btn_url,
            payload=payload,
            allow_comments=allow_comments,
            allow_anonymous=allow_anonymous,
            expires_in=expires_in,
        )

        return from_dict(Invoice, response)

    def transfer(
        self,
        user_id: int,
        asset: Asset,
        amount: str,
        spend_id: str,
        comment: Optional[str] = None,
        disable_send_notification: Optional[bool] = None,
    ) -> Transfer:
        """
        Use this method to send coins from your app's balance to a user.
        On success, returns object of completed transfer.

        :param user_id: Telegram user ID. User must have previously used @CryptoBot (@CryptoTestnetBot for testnet).
        :param asset: Currency code. Supported assets: “BTC”, “TON”, “ETH” (testnet only), “USDT”, “USDC” and “BUSD”.
        :param amount: Amount of the transfer in float. Min $0.1. For example: 125.50
        :param spend_id: Unique ID to make your request idempotent and ensure that only one of the transfers with the same spend_id will be accepted by Crypto Pay API. This parameter is useful when the transfer should be retried (i.e. request timeout, connection reset, 500 HTTP status, etc). It can be some unique withdrawal identifier for example. Up to 64 symbols.
        :param comment: Comment for the transfer. Users will see this comment when they receive a notification about the transfer. Up to 1024 symbols.
        :param disable_send_notification: Pass true if the user should not receive a notification about the transfer. Default is false.
        :return:
        """

        response = self.client.get(
            "transfer",
            user_id=user_id,
            asset=asset,
            amount=amount,
            spend_id=spend_id,
            comment=comment,
            disable_send_notification=disable_send_notification,
        )

        return Transfer(**response)

    def get_invoices(
        self,
        asset: Optional[Asset] = None,
        invoice_ids: Optional[str] = None,
        status: Optional[Status] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> List[Invoice]:
        """
        Use this method to get invoices of your app. On success, returns array of invoices.

        Args:
            asset: Currency codes separated by comma. Supported assets: “BTC”, “TON”, “ETH” (testnet only), “USDT”, “USDC” and “BUSD”. Defaults to all assets.
            invoice_ids: Invoice IDs separated by comma.
            status: Status of invoices to be returned. Available statuses: “active” and “paid”. Defaults to all statuses.
            offset: Offset needed to return a specific subset of invoices. Default is 0.
            count: Number of invoices to be returned. Values between 1-1000 are accepted. Defaults to 100.
            :return:
        """

        response = self.client.get(
            "getInvoices",
            asset=asset,
            invoice_ids=invoice_ids,
            status=status,
            offset=offset,
            count=count,
        )
        items = response["items"]
        return [from_dict(Invoice, i) for i in items if items]

    def get_balance(self):
        """
        Use this method to get a balance of your app. Returns array of assets.

        :return: id
        """
        return self.client.get("getBalance")

    def get_exchange_rates(self):
        """
        Use this method to get exchange rates of supported currencies. Returns array of currencies.

        :return:
        """
        return self.client.get("getExchangeRates")

    def get_currencies(self):
        """
        Use this method to get a list of supported currencies. Returns array of currencies.

        :return:
        """
        return self.client.get("getCurrencies")

    def __getattr__(self, item):
        init, *temp = item.split("_")
        res = "".join([init.lower(), *map(str.title, temp)])
        self.method = res
        return self

    def __call__(self, **kwargs):
        return self.client.get(self.method, params=kwargs)