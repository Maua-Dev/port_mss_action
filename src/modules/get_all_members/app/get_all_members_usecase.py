from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound
class GetAllMembersUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
        
    def __call__(self,user_id: str):
        member = self.repo.get_member(user_id)
        if member is None:
            raise NoItemsFound('user_id')
        
        members = self.repo.get_all_members()

        return members