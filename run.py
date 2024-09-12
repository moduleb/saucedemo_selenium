

import argparse
import logging

from test_api import test_github_repo
from test_purchase import test_purchase_at_saucedemo

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Запуск функций в зависимости от параметров.")
    parser.add_argument('-s', action='store_true', help='Запустить тест сайта saucedemo.com')
    parser.add_argument('-g', action='store_true', help='Запустить тест GitHub API')

    args = parser.parse_args()

    if args.s:
        test_purchase_at_saucedemo()
    elif args.g:
        test_github_repo()
    else:
        print("Необходимо указать -s или -g")

if __name__ == "__main__":
    main()

