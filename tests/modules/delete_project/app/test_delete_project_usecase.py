import pytest
from src.modules.delete_project.app.delete_project_usecase import DeleteProjectUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnregisteredUser
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_DeleteProjectUsecase:
    def test_delete_project_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
        len_before = len(repo.projects)
        
        project = usecase(code='MF', user_id=repo_member.members[0].user_id)
        assert len(repo.projects) == len_before - 1
        assert project.code == 'MF'
        
    def test_delete_project_usecase_no_items_found(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
        with pytest.raises(NoItemsFound):
            project = usecase(code='VT', user_id=repo_member.members[0].user_id)
            
    def test_delete_project_usecase_invalid_code(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
        with pytest.raises(EntityError):
            project = usecase(code='MauaFood', user_id=repo_member.members[0].user_id)
        
                
    def test_delete_project_usecase_invalid_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
        with pytest.raises(UnregisteredUser):
            project = usecase(code='MF', user_id='adsa')
    
    def test_delete_project_usecase_forbidden_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteProjectUsecase(repo=repo, repo_member=repo_member)
        with pytest.raises(ForbiddenAction):
            project = usecase(code='MauaFood', user_id=repo_member.members[2].user_id)