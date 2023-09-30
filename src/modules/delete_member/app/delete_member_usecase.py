from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class DeleteMemberUseCase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
    
    def __call__(self, ra: str):
        if not Member.validate_ra(ra):
            raise EntityError('ra')
        
        member = self.repo.delete_member(ra=ra)
        
        if member is None:
            raise NoItemsFound('member')
        
        return member