class BaseException(Exception):
    ''' Базовый класс для всех ошибок '''
    
    
    
class CriterionNotAcceptable(BaseException):
    ''' Критерий является недопустимым '''


class FilePathOrNameIsIncorrect(BaseException):
    ''' Неверный путь к файлу или имя файла '''
    