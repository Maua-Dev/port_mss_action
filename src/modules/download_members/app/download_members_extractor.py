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
        
        members_dict = [{
                "name": m.name,
                "email_dev": m.email_dev,
                "email": m.email,
                "ra": m.ra,
                "role": m.role.name if hasattr(m.role, 'name') else str(m.role),
                "stack": m.stack.name if hasattr(m.stack, 'name') else str(m.stack),
                "year": m.year,
                "cellphone": m.cellphone,
                "course": m.course.name if hasattr(m.course, 'name') else str(m.course),
                "hired_date": m.hired_date,
                "active": m.active.name if hasattr(m.active, 'name') else str(m.active),
                "deactivated_date": m.deactivated_date,
                "user_id": m.user_id,
                "photo": m.photo
            }
            for m in members
        ]
        return members_dict