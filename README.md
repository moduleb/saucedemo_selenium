![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## Автоматизированные тесты для saucedemo.com и GitHub API

### Описание

Данный проект включает в себя два автоматизированных теста:  
    1. Проверки сценария покупки товара на сайте saucedemo.com с использованием Python и Selenium  
    2. Проверка работы с GitHub API 

### Структура проекта

```
/saucedemo_selenium
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── run.py
├── settings.py
├── test_api
└── test_purchase
```

## Установка
### Клонируйте проект

```shell
git clone https://github.com/moduleb/saucedemo_selenium.git
```

### Перейдите в папку проекта

```shell
cd saucedemo_selenium
```

### Создайте виртуальное окружение
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### Укажите переменные окружения

Создайте файл `.env` в каталоге проекта и добавьте следующие строки:

```
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token
REPO_NAME=your_repository_name
```
> Создать токен можно здесь https://github.com/settings/tokens

### Установите зависимости
```bash
pip install -r requirements.txt
```

---

## Тест для saucedemo.com

#### Цель

Создать автоматический e2e тест для проверки сценария покупки товара на сайте saucedemo.com.

#### Сценарий теста

1. **Авторизация:**
    - Логин: `standard_user`
    - Пароль: `secret_sauce`
2. **Выбор товара:**
    - Выбрать товар (например, "Sauce Labs Backpack") и добавить его в корзину.
3. **Оформление покупки:**
    - Перейти в корзину и убедиться, что товар добавлен.
    - Оформить покупку, заполнив необходимые поля.
    - Завершить покупку.
4. **Проверка:**
    - Убедиться, что покупка завершена успешно.

#### Запуск теста

- Для запуска теста используйте команду:
  ```bash
  python run.py -s
  ```

---

## Тест для GitHub API

#### Цель

Создать автоматический тест для проверки работы с GitHub API на языке Python.

#### Сценарий теста

1. Создание нового публичного репозитория.
2. Проверка списка репозиториев для подтверждения создания.
3. Удаление репозитория.

#### Запуск теста

- Для запуска теста используйте команду:
  ```bash
  python run.py -g
  ```

### Ожидаемый результат

После выполнения тестов вы должны увидеть, что:

- Тест для saucedemo.com успешно проходит все шаги от авторизации до завершения покупки.
- Тест для GitHub API успешно создает, проверяет наличие и удаляет репозиторий.
 и структурировано!
