import pytest
from src.modules.download_projects.app.download_projects_usecase import DownloadProjectsUsecase
from src.modules.download_projects.app.download_projects_controller import DownloadProjectsController
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UserIsNotFromAdmin,UnregisteredUser, UserNotAllowed
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeFile, WrongTypeParameter
class Test_DownloadProjectsUsecase:
    def test_downloads_project_controller_project_code(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        controller = DownloadProjectsController(usecase=usecase)

        project = usecase( user_id=repo_member.members[0].user_id, project_code = "PT",start = 0,  end= 1677067200000  )
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'member_user_id':repo_member.members[0].user_id,
            'project_code': "PT",
            'start': 0,
            'end': 1677067200000
        })
        response = controller(request)

        assert response.status_code == 200
        assert type(project) == str

    def test_downloads_project_controller_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        controller = DownloadProjectsController(usecase=usecase)

        project = usecase( user_id=repo_member.members[0].user_id, member_user_id= repo_member.members[0].user_id,start = 0,  end= 1677067200000  )
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'member_user_id':repo_member.members[0].user_id,
            'project_code': "PT",
            'start': 0,
            'end': 1677067200000
        })
        response = controller(request)

        assert response.status_code == 200
        assert type(project) == str

    def test_downloads_project_controller_no_items_found(self):    
            repo = ActionRepositoryMock()
            repo_member = MemberRepositoryMock()
            usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
            controller = DownloadProjectsController(usecase=usecase)
            with pytest.raises(NoItemsFound):
                project = usecase( user_id=repo_member.members[0].user_id, project_code = "Md",start = 1672531200,  end= 1677067200000  )
                request = HttpRequest(body={
                    "requester_user": {
                        "sub": repo_member.members[0].user_id,
                        "name": repo_member.members[0].name,
                        "email": repo_member.members[0].email,
                        "custom:isMaua": True
                    },
                    'member_user_id':repo_member.members[0].user_id,
                    'project_code': "Md",
                    'start': 1672531200,
                    'end': 1677067200000
                })
                response = controller(request)
                assert response.status_code == 404

    def test_downloads_project_controller_invalid_code(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        controller = DownloadProjectsController(usecase=usecase)
        with pytest.raises(EntityError):
            project = usecase( user_id=repo_member.members[0].user_id, project_code = "MauaFood",start = 0,  end= 1677067200000  )
            request = HttpRequest(body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
                },
                'member_user_id':repo_member.members[0].user_id,
                'project_code': "MauaFood",
                'start': 0,
                'end': 1677067200000
            })
            response = controller(request)
            assert response.status_code == 400

    def test_downloads_project_controller_invalid_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        controller = DownloadProjectsController(usecase=usecase)
        with pytest.raises(EntityError):
            project = usecase( user_id='1', project_code = "PT",start = 0,  end= 1677067200000  )
            request = HttpRequest(body={
                "requester_user": {
                    "sub": '1',
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
                },
                'member_user_id':repo_member.members[0].user_id,
                'project_code': "PT",
                'start': 0,
                'end': 1677067200000
            })
            response = controller(request)
            assert response.status_code == 400

    def test_downloads_project_controller_DISCONNECTED_member(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        controller = DownloadProjectsController(usecase=usecase)
        repo_member.members[0].active = ACTIVE.DISCONNECTED
        with pytest.raises(UserNotAllowed):
            project = usecase( user_id=repo_member.members[0].user_id, project_code = "PT",start = 0,  end= 1677067200000  )
            request = HttpRequest(body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
                },
                'member_user_id':repo_member.members[0].user_id,
                'project_code': "PT",
                'start': 0,
                'end': 1677067200000
            })
            response = controller(request)
            assert response.status_code == 400
        
    def test_downloads_project_controller_member_not_admin(self):
            repo = ActionRepositoryMock()
            repo_member = MemberRepositoryMock()
            usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
            controller = DownloadProjectsController(usecase=usecase)
            repo_member.members[0].role = ROLE.DEV
            with pytest.raises(UserIsNotFromAdmin):
                project = usecase( user_id=repo_member.members[0].user_id, project_code = "PT",start = 0,  end= 1677067200000  )
                request = HttpRequest(body={
                    "requester_user": {
                        "sub": repo_member.members[0].user_id,
                        "name": repo_member.members[0].name,
                        "email": repo_member.members[0].email,
                        "custom:isMaua": True
                    },
                    'member_user_id':repo_member.members[0].user_id,
                    'project_code': "PT",
                    'start': 0,
                    'end': 1677067200000
                })
                response = controller(request)
                assert response.status_code == 400
        
    def test_downloads_project_controller_start_higher_than_end(self):
            repo = ActionRepositoryMock()
            repo_member = MemberRepositoryMock()
            usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
            controller = DownloadProjectsController(usecase=usecase)
            with pytest.raises(ForbiddenAction):
                project = usecase( user_id=repo_member.members[0].user_id, project_code = "PT",start = 1677067200000,  end= 0  )
                request = HttpRequest(body={
                    "requester_user": {
                        "sub": repo_member.members[0].user_id,
                        "name": repo_member.members[0].name,
                        "email": repo_member.members[0].email,
                        "custom:isMaua": True
                    },
                    'member_user_id':repo_member.members[0].user_id,
                    'project_code': "PT",
                    'start': 1677067200000,
                    'end': 0
                })
                response = controller(request)
                assert response.status_code == 400

    def test_downloads_project_controller_missing_parameters(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        controller = DownloadProjectsController(usecase=usecase)
     
        project = usecase( user_id=repo_member.members[0].user_id, project_code = "PT",start = 0,  end= 1677067200000  )
        request = HttpRequest(body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
                },
          
                'project_code': "PT",
                'start': 0,
            })
        response = controller(request)
        assert response.status_code == 400
    

        