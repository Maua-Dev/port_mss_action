from src.shared.helpers.errors.base_error import BaseError


class EntityError(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Field {message} is not valid')

class EntityParameterTypeError(EntityError):
    def __init__(self, message: str):
        super().__init__(message)
        self.__message = message

    @property
    def message(self):
        return self.__message

class EntityParameterError(EntityError):
    def __init__(self, message: str):
        super().__init__(message)
        self.__message = message

    @property
    def message(self):
        return self.__message

class DuplicatedItem(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Item with {message} already exists')
        self.__message = message
    
    @property
    def message(self):
        return self.__message
    
class ItemNotFound(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Item with {message} not found')
        self.__message = message
    
    @property
    def message(self):
        return self.__message
    
class MissingParameters(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Missing parameters: {message}')
        self.__message = message
    
    @property
    def message(self):
        return self.__message
    
    