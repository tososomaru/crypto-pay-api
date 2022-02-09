import os

from dotenv import load_dotenv


class TestEnvConfig:
    base_url = "https://testnet-pay.crypt.bot/api/"


class ProductionEnvConfig:
    base_url = "https://pay.crypt.bot/api/"


env_config = {
    "test": TestEnvConfig,
    "prod": ProductionEnvConfig
}

load_dotenv()
app_config = env_config[os.getenv("environment_type")]()
