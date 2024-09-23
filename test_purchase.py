"""
Тест покупки на сайте saucedemo.com
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


def login(driver: webdriver, site_login: str, site_password: str) -> None:
    logger.info('Авторизация...')
    driver.find_element(By.ID, "user-name").send_keys(site_login)
    driver.find_element(By.ID, "password").send_keys(site_password)
    driver.find_element(By.ID, "login-button").click()


def select_product(driver: webdriver, product_name: str) -> None:
    logger.info('Выбор товара...')
    product = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//div[@class='inventory_item' and contains(., '{product_name}')]")))
    product.find_element(By.TAG_NAME, "button").click()


def go_to_cart(driver: webdriver) -> None:
    logger.info('Переход в корзину...')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))
    ).click()


def assert_product_in_cart(driver: webdriver, product_name: str) -> None:
    logger.info("Проверка, что товар добавлен в корзину...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//div[@class='cart_item' and contains(., '{product_name}')]"))
    )


def fill_checkout_form(driver: webdriver, first_name, last_name, postal_code) -> None:
    logger.info("Заполнение формы...")

    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()


def checkout(driver: webdriver) -> None:
    logger.info("формление покупки...")

    driver.find_element(By.XPATH, "//button[@id='checkout']").click()


def complete_purchase(driver: webdriver) -> None:
    logger.info("Завершение покупки...")

    driver.find_element(By.XPATH, "//button[@id='finish']").click()


def assert_purchase_success(driver: webdriver) -> bool:
    logger.info("Проверка успешного завершения покупки...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='Thank you for your order!']"))
    )


def test_purchase_at_saucedemo() -> None:
    site_login = 'standard_user'
    site_password = 'secret_sauce'
    site_url = 'https://saucedemo.com'
    product_name = 'Sauce Labs Backpack'

    first_name = "John"
    last_name = "Doe"
    postal_code = "12345"

    with webdriver.Firefox() as driver:
        try:
            driver.get(site_url)
            login(driver, site_login, site_password)
            select_product(driver, product_name)
            go_to_cart(driver)
            assert_product_in_cart(driver, product_name)
            checkout(driver)
            fill_checkout_form(driver, first_name, last_name, postal_code)
            complete_purchase(driver)
            assert_purchase_success(driver)
            logger.info("'test_purchase_at_saucedemo' is successful")

        except Exception as e:
            logger.error(f"Test {'test_purchase_at_saucedemo'} failed\n"
                         f"Error: {str(e)}")
