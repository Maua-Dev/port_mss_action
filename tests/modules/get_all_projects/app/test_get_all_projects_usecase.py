from src.modules.get_all_projects.app.get_all_projects_usecase import GetAllProjectsUsecase
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_GetAllProjectsUsecase:
    def test_get_all_projects_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetAllProjectsUsecase(repo=repo, repo_member=repo_member)
        
        projects = usecase(repo_member.members[0].user_id)
        assert type(projects) == list
        assert len(projects) == 5
        assert type(projects[0]) == Project