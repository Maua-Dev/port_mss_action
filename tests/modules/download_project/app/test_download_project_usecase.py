import pytest
from src.modules.download_projects.app.download_projects_usecase import DownloadProjectsUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UserIsNotFromAdmin,UnregisteredUser, UserNotAllowed
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.role_enum import ROLE
class Test_DownloadProjectsUsecase:
    def test_downloads_project_usecase_project_code(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        
        project = usecase( user_id=repo_member.members[0].user_id, project_code = "PT",start = 0,  end= 1677067200000  )
        
        assert type(project) == str

    def test_downloads_project_usecase_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        
        project = usecase( user_id=repo_member.members[0].user_id, member_user_id= repo_member.members[0].user_id,start = 0,  end= 1677067200000  )
        
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
    
    def test_downloads_project_usecase_invalid_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        with pytest.raises(EntityError):
            project = usecase( user_id='1', project_code = "PT",start = 0,  end= 1677067200000  )
    
    def test_downloads_project_usecase_invalid_member_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        repo_member.members[0].active = ACTIVE.DISCONNECTED
        with pytest.raises(UserNotAllowed):
            project = usecase( user_id=repo_member.members[0].user_id, project_code = "PT",start = 0,  end= 1677067200000  )
    
    def test_downloads_project_usecase_member_not_admin(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
        repo_member.members[0].role = ROLE.DEV
        with pytest.raises(UserIsNotFromAdmin):
            project = usecase( user_id=repo_member.members[0].user_id, project_code = "PT",start = 0,  end= 1677067200000  )
    
    def test_downloads_project_usecase_start_higher_than_end(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DownloadProjectsUsecase(repo=repo, repo_member=repo_member)
  
        with pytest.raises(ForbiddenAction):
            project = usecase( user_id=repo_member.members[0].user_id, project_code = "PT",start = 1677067200000,  end= 0  )
