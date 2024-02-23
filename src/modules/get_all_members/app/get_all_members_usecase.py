from src.shared.domain.repositories.member_repository_interface import IMemberRepository

class GetAllMembersUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
        
    def __call__(self):
        members = self.repo.get_all_members()
    
        return members