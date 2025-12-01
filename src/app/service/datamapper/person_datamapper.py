from src.app.service.datamapper.base_datamapper import BaseDataMapper
from src.app.models.person import Person


class PersonDataMapper(BaseDataMapper):
    model = Person
    
    