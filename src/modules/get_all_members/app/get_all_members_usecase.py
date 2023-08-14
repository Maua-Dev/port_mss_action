from src.shared.domain.repositories.action_repository_interface import IActionRepository

class GetAllMembersUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self):
        members = self.repo.get_all_members()
    
        return members