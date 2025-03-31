from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class DownloadMembersExtractor:

    def __init__(self, repo: IMemberRepository):
        self.repo_member = repo

    def __call__(self):
        
        try:
            members = self.repo_member.get_all_members()
        except:
            raise NoItemsFound('members')
        
        return members