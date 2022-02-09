from dataclasses import dataclass
from typing import Optional


@dataclass
class Invoice:
    """Invoice object.


    Args:
        invoice_id (int): Unique ID for this invoice.
        status (str): Status of the invoice, can be either “active”, “paid” or “expired”.
        hash (str): Hash of the invoice.
        asset (str): Currency code. Currently, can be “BTC”, “TON”, “ETH” (testnet only), “USDT”, “USDC” or “BUSD”.
        amount (str): Amount of the invoice.
        pay_url (str): URL should be presented to the user to pay the invoice.
        description (Optional[str]): Description for this invoice.
        created_at: (str): Date the invoice was created in ISO 8601 format.
        allow_comments: (str): True, if the user can add comment to the payment.
        allow_anonymous: (Optional[str]): True, if the user can pay the invoice anonymously.
        expiration_date: (Optional[str]): Date the invoice was paid in Unix time.
        paid_at: (Optional[str]): Date the invoice was paid in Unix time.
        paid_anonymously: (Optional[bool]): True, if the invoice was paid anonymously.
        comment: (Optional[str]): Comment to the payment from the user.
        hidden_message: (Optional[str]): Text of the hidden message for this invoice.
        payload: (Optional[str]): Previously provided data for this invoice.
        paid_btn_name: (Optional[str]): Name of the button, can be “viewItem”, “openChannel”, “openChannel” or “callback”.
        paid_btn_url: (Optional[str]): URL of the button.
    """

    invoice_id: int
    status: str
    hash: str
    asset: str
    amount: str
    pay_url: str
    description: Optional[str]
    created_at: str
    allow_comments: bool
    allow_anonymous: bool
    expiration_date: Optional[str]
    paid_at: Optional[str]
    paid_anonymously: Optional[bool]
    comment: Optional[str]
    hidden_message: Optional[str]
    payload: Optional[str]
    paid_btn_name: Optional[str]
    paid_btn_url: Optional[str]


@dataclass
class Transfer:
    """ Transfer object.

    Args:
        transfer_id: (int): Unique ID for this transfer.
        user_id: (str): Telegram user ID the transfer was sent to.
        asset: (str): Currency code. Currently, can be “BTC”, “TON”, “ETH” (testnet only), “USDT”, “USDC” or “BUSD”.
        amount: (str): Amount of the transfer.
        status: (str): Status of the transfer, can be “completed”.
        completed_at: (str): Date the transfer was completed in ISO 8601 format.
        comment: (Optional[str]): Comment for this transfer.
    """
    transfer_id: int
    user_id: str
    asset: str
    amount: str
    status: str
    completed_at: str
    comment: Optional[str]
