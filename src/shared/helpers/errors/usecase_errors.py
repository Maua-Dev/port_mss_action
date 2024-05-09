from src.shared.helpers.errors.base_error import BaseError

class NoItemsFound(BaseError):
    def __init__(self, message: str):
        super().__init__(f'No items found for {message}')

class DuplicatedItem(BaseError):
    def __init__(self, message: str):
        super().__init__(f'The item alredy exists for this {message}')
        
class ForbiddenAction(BaseError):
    def __init__(self, message: str):
        super().__init__(f'That action is forbidden for this {message}')

class UserNotAllowed(BaseError):
    def __init__(self):
        super().__init__(f'That type of user has no permission for that action')

class UnregisteredUser(BaseError):
    def __init__(self):
        super().__init__(f'That user is not registered')

class PaginationAmountInvalid(BaseError):
    def __init__(self):
        super().__init__(f'The amount must be greater or equal than 10')

