from src.modules.get_all_projects.app.get_all_projects_controller import GetAllProjectsController
from src.modules.get_all_projects.app.get_all_projects_usecase import GetAllProjectsUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_GetAllProjectsController:
    def test_get_all_projects_controller(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetAllProjectsUsecase(repo=repo, repo_member=repo_member)
        controller = GetAllProjectsController(usecase=usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
        })
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['message'] == 'the projects were retrieved'
        assert len(response.body['projects']) == len(repo.projects)