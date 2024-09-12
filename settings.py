"""
Создание конфигурации, загрузка переменных из файла .env
"""

import logging

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Загружаем переменные из файла '.env'
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    GITHUB_TOKEN: str = 'your_token_here'
    GITHUB_API_URL: str = 'https://api.github.com/user/repos'
    GITHUB_USERNAME: str
    REPO_NAME: str # имя репозитория

    # Уровень логирования по умолчанию
    log_level: str = 'INFO'


settings = Settings()

# Настройка базового уровня логирования
logging.basicConfig(level=logging.getLevelName(settings.log_level))
