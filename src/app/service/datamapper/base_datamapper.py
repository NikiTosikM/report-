from typing import TypeVar

from src.app.models.base_model import BaseModel


Model = TypeVar("Model", bound=BaseModel)


class BaseDataMapper:
    model: type[Model]
    
    @classmethod
    def map_to_persistence_entity(cls, data: dict):
        ''' Сериализация словаря в модель '''
        
        return cls.model(
            *data.values()
        )