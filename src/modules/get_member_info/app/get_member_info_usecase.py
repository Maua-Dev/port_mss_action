from typing import List
from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed

class GetMemberInfoUsecase:
    def __init__(self, member_repo: IMemberRepository, action_repo: IActionRepository):
        self.member_repo = member_repo
        self.action_repo = action_repo

    def __call__(self, requester_user_id: str) -> List[Member]:
        if not Member.validate_user_id(requester_user_id):
            raise EntityError('user_id')

        requester = self.member_repo.get_member(user_id=requester_user_id)

        if requester is None:
            raise UnregisteredUser()

        if not Member.validate_active(requester.active):
            raise UserNotAllowed()

        all_members = self.member_repo.get_all_members()

        projects = self.action_repo.get_all_projects()

        for member in all_members:
            member_projects = []
            for project in projects:
                if member.user_id in project.members_user_ids:
                    member_projects.append(project.name)

            member.project = member_projects

        return all_members