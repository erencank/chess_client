import logging

from pydantic import WebsocketUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

# Configure the logger
logger = logging.getLogger("chess_bot")
logger.setLevel(logging.INFO)  # Set the logging level to INFO

# Create a console handler and set the level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    bot_token: str
    backend_ws_url: WebsocketUrl


settings = Settings()  # type: ignore
