import csv
import os

from src.app.exceptions.exceptions import FilePathOrNameIsIncorrect, CriterionNotAcceptable
from src.app.service.datamapper.person_datamapper import PersonDataMapper
from src.app.models.person import Person

class CsvReader:
    """Класс для получения информации из файла"""

    def __init__(self, files: list[str], criteria: str):
        self.names_files = files
        self.criteria = self.criterion_check(criteria)
        
    def criterion_check(cls, criteria: str):
        ''' Проверка критерия '''
        
        acceptable_criteria = ["performance"] # список допустимых критериев
        
        if criteria not in acceptable_criteria:
            raise CriterionNotAcceptable(f"Критерий {criteria} недопустим. Выберете другой ")
        
        return criteria

    def read_file(self, file: str) -> list[dict]:
        """Читает содержимое файла"""
        
        # проверяем наличие файла
        if not os.path.exists(file):
            file_in_files = os.path.join("csv_files", file)
            if os.path.exists(file_in_files):
                file = file_in_files
            else:
                raise FilePathOrNameIsIncorrect(f"Файл {file} не был найден ")

        try:
            file_contents: list[dict] = []

            with open(file, mode="r", newline="", encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    file_contents.append(row)

            return file_contents

        except FileNotFoundError:
            raise FilePathOrNameIsIncorrect(f"Файл {file} не был найден")
        
    def processing_all_information(self) -> list[Person]:
        """ Проходится по файлам и получает всю информацию из них """
        
        files_contents = []
        list_files = self.names_files
        
        for file in list_files:
            info_received: list[dict] = self.read_file(file)
            
            for person in info_received:
                person_model = PersonDataMapper.map_to_persistence_entity(person)
                files_contents.append(person_model)
            
        return files_contents
