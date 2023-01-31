from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem


class CreateMemberUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
    
    def __call__(self, member: Member) -> Member:
        
        if self.repo.get_member(ra=member.ra) is not None:
            raise DuplicatedItem('ra')
        
        return self.repo.create_member(member)
    