import argparse
from argparse import Namespace


class ParserArguments:
    """' Класс считывает аргументы и их значения при запуске скрипта"""

    parser = argparse.ArgumentParser()

    @classmethod
    def add_args(cls) -> None:
        """Добавление аргументов"""

        cls.parser.add_argument(
            "-f",
            "--files",
            help="Путь до файла(ов)/название файла(ов)",
            required=True,
            nargs="+",
        )
        cls.parser.add_argument(
            "-r",
            "--report",
            help="По какому критерию делаетя отчет",
            required=True,
            type=str,
        )

    @classmethod
    def get_args_and_value(cls) -> Namespace:
        """Получение аргументов и их значений"""

        args_and_value: Namespace = cls.parser.parse_args()

        return args_and_value
