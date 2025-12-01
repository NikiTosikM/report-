from dataclasses import dataclass


@dataclass
class Person:
    ''' Дата-класс, который хранит всю информацию о рабочем '''
    
    name: str
    position: str
    completed_tasks: int
    performance: int
    skills: str
    team: str
    experience_years: int