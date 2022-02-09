from strenum import StrEnum


class Asset(StrEnum):
    BTC = "BTC"
    TON = "TON"
    ETH = "ETH"
    USDT = "USDT"
    USDC = "USDC"
    BUSD = "BUSD"


class Button(StrEnum):
    VIEW_ITEM = "viewItem"
    OPEN_CHANNEL = "openChannel"
    OPEN_BOT = "openBot"
    CALLBACK = "callback"


class Status(StrEnum):
    ACTIVE = "active"
    PAID = "paid"
