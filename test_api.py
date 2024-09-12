"""
Test GitHb API
"""

import json
import logging

import requests

from settings import settings

logger = logging.getLogger(__name__)

GITHUB_TOKEN = settings.GITHUB_TOKEN
GITHUB_API_URL = 'https://api.github.com/user/repos'
GITHUB_USERNAME = settings.GITHUB_USERNAME
repo_name = settings.REPO_NAME

# Заголовки для аутентификации
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def create_repository(repo_name):
    """Создает новый публичный репозиторий."""
    data = {
        'name': repo_name,
        'private': False
    }
    response = requests.post(GITHUB_API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        logger.info(f'Репозиторий "{repo_name}" успешно создан.')
    else:
        logger.warning(f'Ошибка при создании репозитория: {response.json()}')


def check_repository_exists(repo_name):
    """Проверяет наличие репозитория."""

    response = requests.get(GITHUB_API_URL, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            if repo['name'] == repo_name:
                logger.info(f'Репозиторий "{repo_name}" существует.')
                return True
        logger.warning(f'Репозиторий "{repo_name}" не найден.')
        return False
    else:
        logger.warning(f'Ошибка при получении списка репозиториев: {response.json()}')
        return False


def delete_repository(repo_name):
    """Удаляет репозиторий."""

    delete_url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}'
    response = requests.delete(delete_url, headers=headers)
    if response.status_code == 204:
        logger.info(f'Репозиторий "{repo_name}" успешно удален.')
    else:
        logger.warning(f'Ошибка при удалении репозитория: {response.json()}')


def test_github_repo():
    create_repository(repo_name)
    if check_repository_exists(repo_name):
        delete_repository(repo_name)
