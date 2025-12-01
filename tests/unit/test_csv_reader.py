import pytest

from src.app.service.bussines.file_reader import CsvReader
from src.app.exceptions.exceptions import CriterionNotAcceptable


class TestCsvReader:
    
    def test_criterion_check_valid(self):
        """Тест проверки допустимого критерия"""
        reader = CsvReader(files=["test.csv"], criteria="performance")
        assert reader.criteria == "performance"
    
    def test_criterion_check_invalid(self):
        """Тест проверки недопустимого критерия"""
        with pytest.raises(CriterionNotAcceptable) as exc_info:
            CsvReader(files=["employees1.csv"], criteria="invalid_criteria")
        assert "недопустим" in str(exc_info.value)