from src.modules.portfolio_export_members.app.portfolio_export_members_usecase import PortfolioExportMembersUsecase
from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_PortfolioExportMembersUsecase:
    def test_portfolio_export_members_usecase(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = PortfolioExportMembersUsecase(member_repo=member_repo, action_repo=action_repo)

        members = usecase()

        assert type(members) == list
        assert len(members) > 0
        assert type(members[0]) == Member

        member_with_projects = next((m for m in members if m.name == 'Vitor Guirão MPNTM'), None)
        assert member_with_projects is not None
        assert hasattr(member_with_projects, 'project')
        assert isinstance(member_with_projects.project, list)
        assert len(member_with_projects.project) > 0

    def test_portfolio_export_members_usecase_returns_all_members(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = PortfolioExportMembersUsecase(member_repo=member_repo, action_repo=action_repo)

        members = usecase()

        assert len(members) == len(member_repo.members)
        assert [m.user_id for m in members] == [m.user_id for m in member_repo.members]

    def test_portfolio_export_members_usecase_attaches_project_to_every_member(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = PortfolioExportMembersUsecase(member_repo=member_repo, action_repo=action_repo)

        members = usecase()

        for member in members:
            assert hasattr(member, 'project')
            assert isinstance(member.project, list)

    def test_portfolio_export_members_usecase_projects_match_membership(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = PortfolioExportMembersUsecase(member_repo=member_repo, action_repo=action_repo)

        members = usecase()

        for member in members:
            expected_projects = [
                project.name
                for project in action_repo.projects
                if member.user_id in project.members_user_ids
            ]
            assert member.project == expected_projects

    def test_portfolio_export_members_usecase_member_without_projects(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        action_repo.projects = []
        usecase = PortfolioExportMembersUsecase(member_repo=member_repo, action_repo=action_repo)

        members = usecase()

        assert len(members) > 0
        for member in members:
            assert member.project == []
