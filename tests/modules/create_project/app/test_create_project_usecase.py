import pytest
from src.modules.create_project.app.create_project_usecase import CreateProjectUsecase
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.errors.usecase_errors import DuplicatedItem


class Test_CreateProjectUsecase:
    def test_create_project_usecase(self):
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        lenBefore = len(repo.projects)
        
        project = usecase(code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', scrum_user_id='7465hvnb-143g-1675-86HnG-75hgnFbcg36', start_date=1649955600000, photos=['https://i.imgur.com/7QF7uCk.png'], members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36'])

        assert len(repo.projects) == lenBefore + 1
        assert project == repo.projects[-1]
        assert repo.projects[-1].code == 'DM'
        assert repo.projects[-1].photos == ['https://i.imgur.com/7QF7uCk.png']
        
    def test_create_project_usecase_without_photos(self):
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        lenBefore = len(repo.projects)
        
        project = usecase(code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', scrum_user_id='7465hvnb-143g-1675-86HnG-75hgnFbcg36', start_date=1649955600000, members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36'])

        assert len(repo.projects) == lenBefore + 1
        assert project == repo.projects[-1]
        assert repo.projects[-1].code == 'DM'
        assert repo.projects[-1].photos == []

    def test_create_project_usecase_duplicated_code(self):
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        lenBefore = len(repo.projects)
        
        with pytest.raises(DuplicatedItem):
            project = usecase(code="PT",
                name="Portfólio",
                description="É um site",
                po_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                scrum_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                start_date=1673535600000,
                photos=["https://i.imgur.com/gHoRKJU.png"],
                members_user_ids=["6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ])