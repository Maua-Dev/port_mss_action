from src.modules.create_project.app.create_project_usecase import CreateProjectUsecase
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_CreateProjectUsecase:
    def test_create_project_usecase(self):
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        lenBefore = len(repo.projects)
        
        project = usecase(code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_RA='21021031', scrum_RA='17033730', start_date=1649955600000, photos=['https://i.imgur.com/7QF7uCk.png'])
        assert len(repo.projects) == lenBefore + 1
        assert project == repo.projects[-1]
        assert repo.projects[-1].code == 'DM'
        assert repo.projects[-1].photos == ['https://i.imgur.com/7QF7uCk.png']
        
    def test_create_project_usecase_without_photos(self):
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        lenBefore = len(repo.projects)
        
        project = usecase(code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_RA='21021031', scrum_RA='17033730', start_date=1649955600000)
        assert len(repo.projects) == lenBefore + 1
        assert project == repo.projects[-1]
        assert repo.projects[-1].code == 'DM'
        assert repo.projects[-1].photos == []