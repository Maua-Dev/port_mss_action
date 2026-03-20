from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed


class GetMemberInfoUsecase:
    def __init__(self, member_repo: IMemberRepository, action_repo: IActionRepository):
        self.member_repo = member_repo
        self.action_repo = action_repo

    def __call__(self, user_id: str) -> Member:

        if not Member.validate_user_id(user_id):
            raise EntityError('user_id')

        member = self.member_repo.get_member(user_id=user_id)

        if member is None:
            raise UnregisteredUser()

        is_active = Member.validate_active(member.active)

        if not is_active:
            raise UserNotAllowed()

        # Puxa os projetos do membro para incluir no portfólio
        projects = self.action_repo.get_all_projects()
        member_projects = []

        for project in projects:
            if member.user_id in project.members_user_ids:
                member_projects.append(project.name)

        member.project = member_projects

        return member