from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class GetMemberUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, ra: str) -> Member:
        
        if not Member.validate_ra(ra):
            raise EntityError('ra')
        
        member = self.repo.get_member(ra)
        
        if member == None:
            raise NoItemsFound('member')
        
        return member