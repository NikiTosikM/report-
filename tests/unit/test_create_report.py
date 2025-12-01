from src.app.models.person import Person
from src.app.service.bussines.create_report import CreateReport

class TestCreateReport:
    def test_computing_performance_basic(self):
        """Тест расчета средней эффективности"""
        
        persons = [
            Person(name="Никита", position="разработчик", performance=5.0, 
                   completed_tasks=10, skills="Python", team="A", experience_years=3),
            Person(name="Павел", position="разработчик", performance=3.5, 
                   completed_tasks=12, skills="Java", team="A", experience_years=5),
            Person(name="Виктория", position="тестировщик", performance=4.2, 
                   completed_tasks=8, skills="Testing", team="B", experience_years=2),
        ]
        
        report = CreateReport(persons_info=persons)
        result = report.computing_performance(criteria="performance")
        
        assert len(result) == 2
        assert result[0][0] == "разработчик"
        assert result[0][1] == 4.25
        assert result[1][1] == 4.2
    
    def test_computing_performance_empty_list(self):
        """Тест с пустым списком сотрудников"""
        report = CreateReport(persons_info=[])
        result = report.computing_performance(criteria="performance")
        
        assert result == []