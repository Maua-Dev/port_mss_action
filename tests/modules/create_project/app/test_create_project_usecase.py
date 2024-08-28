import pytest
from src.modules.create_project.app.create_project_usecase import CreateProjectUsecase
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, UnregisteredUser, UserNotAllowed
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE

class Test_CreateProjectUsecase:
    def test_create_project_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        lenBefore = len(repo.projects)
        
        project = usecase(user_id=repo_member.members[0].user_id, code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', scrum_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', start_date=1649955600000, photos=['https://i.imgur.com/7QF7uCk.png'], members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'])

        assert len(repo.projects) == lenBefore + 1
        assert project == repo.projects[-1]
        assert repo.projects[-1].code == 'DM'
        assert repo.projects[-1].photos == ['https://i.imgur.com/7QF7uCk.png']
        
    def test_create_project_usecase_without_photos(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        lenBefore = len(repo.projects)
        
        project = usecase(user_id=repo_member.members[0].user_id, code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', scrum_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', start_date=1649955600000, members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'])

        assert len(repo.projects) == lenBefore + 1
        assert project == repo.projects[-1]
        assert repo.projects[-1].code == 'DM'
        assert repo.projects[-1].photos == []

    def test_create_project_usecase_duplicated_code(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        
        with pytest.raises(DuplicatedItem):
            project = usecase(user_id=repo_member.members[0].user_id,
                code="PT",
                name="Portfólio",
                description="É um site",
                po_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                scrum_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                start_date=1673535600000,
                photos=["https://i.imgur.com/gHoRKJU.png"],
                members_user_ids=["6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3","5f55f6a5-a66e-4fff-9faf-72cd478bd5a0"])
    
    def test_create_project_unregistered_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        
        with pytest.raises(UnregisteredUser):
            project = usecase(user_id="aadas",
                code="PT",
                name="Portfólio",
                description="É um site",
                po_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                scrum_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                start_date=1673535600000,
                photos=["https://i.imgur.com/gHoRKJU.png"],
                members_user_ids=["6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3","5f55f6a5-a66e-4fff-9faf-72cd478bd5a0"])
    
    def test_create_project_forbidden_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        repo_member.members[2].active = ACTIVE.ACTIVE
        with pytest.raises(UserNotAllowed):
            project = usecase(user_id=repo_member.members[2].user_id,
                code="PT",
                name="Portfólio",
                description="É um site",
                po_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                scrum_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                start_date=1673535600000,
                photos=["https://i.imgur.com/gHoRKJU.png"],
                members_user_ids=["6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3","5f55f6a5-a66e-4fff-9faf-72cd478bd5a0"])
    
    def test_create_project_usecase_po_is_FREEZE(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        lenBefore = len(repo.projects)
        po = repo_member.get_member('5f55f6a5-a66e-4fff-9faf-72cd478bd5a0')
        po.active= ACTIVE.FREEZE

        with pytest.raises(ForbiddenAction):
            usecase(user_id=repo_member.members[0].user_id, code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id=po.user_id, scrum_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', start_date=1649955600000, photos=['https://i.imgur.com/7QF7uCk.png'], members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'])

    def test_create_project_usecase_po_is_DISCONNECTED(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        lenBefore = len(repo.projects)
        po = repo_member.get_member('5f55f6a5-a66e-4fff-9faf-72cd478bd5a0')
        po.active= ACTIVE.DISCONNECTED

        with pytest.raises(ForbiddenAction):
            usecase(user_id=repo_member.members[0].user_id, code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id=po.user_id, scrum_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', start_date=1649955600000, photos=['https://i.imgur.com/7QF7uCk.png'], members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'])

    def test_create_project_usecase_scrum_is_FREEZE(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        lenBefore = len(repo.projects)
        scrum = repo_member.get_member('5f55f6a5-a66e-4fff-9faf-72cd478bd5a0')
        scrum.active= ACTIVE.FREEZE

        with pytest.raises(ForbiddenAction):
            usecase(user_id=repo_member.members[0].user_id, code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', scrum_user_id=scrum.user_id, start_date=1649955600000, photos=['https://i.imgur.com/7QF7uCk.png'], members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'])


    def test_create_project_usecase_scrum_is_DISCONNECTED(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        lenBefore = len(repo.projects)
        scrum = repo_member.get_member('5f55f6a5-a66e-4fff-9faf-72cd478bd5a0')
        scrum.active= ACTIVE.DISCONNECTED

        with pytest.raises(ForbiddenAction):
            usecase(user_id=repo_member.members[0].user_id, code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', scrum_user_id=scrum.user_id, start_date=1649955600000, photos=['https://i.imgur.com/7QF7uCk.png'], members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'])



    def test_create_project_usecase_user_is_FREEZE(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        lenBefore = len(repo.projects)
        user = repo_member.members[0]
        user.active= ACTIVE.FREEZE

        with pytest.raises(ForbiddenAction):
            usecase(user_id=repo_member.members[0].user_id, code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', scrum_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', start_date=1649955600000, photos=['https://i.imgur.com/7QF7uCk.png'], members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'])


    def test_create_project_usecase_user_is_DISCONNECTED(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        lenBefore = len(repo.projects)
        user = repo_member.members[0]
        user.active= ACTIVE.DISCONNECTED

        with pytest.raises(ForbiddenAction):
            usecase(user_id=repo_member.members[0].user_id, code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', scrum_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', start_date=1649955600000, photos=['https://i.imgur.com/7QF7uCk.png'], members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'])


