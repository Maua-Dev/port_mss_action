import pytest
from src.modules.download_projects.app.download_projects_usecase import DownloadProjectsUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnregisteredUser, UserNotAllowed
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE

class Test_DownloadProjectsUsecase:
    def test_downloads_project_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        
        project = usecase( user_id=repo_member.members[0].user_id, project_code = "PT",start = 0,  end= 1677067200000  )
        
        assert type(project) == str
    
    def test_downloads_project_usecase_no_items_found(self):    
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        with pytest.raises(NoItemsFound):
            project = usecase( user_id=repo_member.members[0].user_id, project_code = "Md",start = 1672531200,  end= 1677067200000  )
   
    def test_downloads_project_usecase_invalid_code(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        with pytest.raises(EntityError):
            project = usecase( user_id=repo_member.members[0].user_id, project_code = "MauaFood",start = 0,  end= 1677067200000  )

    # def test_delete_project_usecase_no_items_found(self):
    #     repo = ActionRepositoryMock()
    #     repo_member = MemberRepositoryMock()
    #     usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
    #     with pytest.raises(NoItemsFound):
    #         project = usecase(code='VT', user_id=repo_member.members[0].user_id)
            
    # def test_delete_project_usecase_invalid_code(self):
    #     repo = ActionRepositoryMock()
    #     repo_member = MemberRepositoryMock()
    #     usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
    #     with pytest.raises(EntityError):
    #         project = usecase(code='MauaFood', user_id=repo_member.members[0].user_id)
        
                
    # def test_delete_project_usecase_invalid_user_id(self):
    #     repo = ActionRepositoryMock()
    #     repo_member = MemberRepositoryMock()
    #     usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
    #     with pytest.raises(UnregisteredUser):
    #         project = usecase(code='MF', user_id='adsa')
    
    # def test_delete_project_usecase_forbidden_user(self):
    #     repo = ActionRepositoryMock()
    #     repo_member = MemberRepositoryMock()
    #     usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
    #     with pytest.raises(UserNotAllowed):
    #         project = usecase(code='MauaFood', user_id=repo_member.members[2].user_id)
    
    # def test_delete_project_usecase_FREEZE_user(self):
    #     repo = ActionRepositoryMock()
    #     repo_member = MemberRepositoryMock()
    #     usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
    #     user = repo_member.members[0]
    #     user.active= ACTIVE.FREEZE
    #     with pytest.raises(UserNotAllowed):
    #         usecase(code='MauaFood', user_id=user.user_id)
    
    # def test_delete_project_usecase_DISCONNECTED_user(self):
    #     repo = ActionRepositoryMock()
    #     repo_member = MemberRepositoryMock()
    #     usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
    #     user = repo_member.members[0]
    #     user.active= ACTIVE.DISCONNECTED
    #     with pytest.raises(UserNotAllowed):
    #         usecase(code='MauaFood', user_id=user.user_id)