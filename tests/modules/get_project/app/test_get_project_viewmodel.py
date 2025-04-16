from src.modules.get_project.app.get_project_usecase import GetProjectUsecase
from src.modules.get_project.app.get_project_viewmodel import GetProjectViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_GetProjectViewmodel:
    def test_get_project_viewmodel(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetProjectUsecase(repo=repo, repo_member=repo_member)
        project = usecase(code='MF', user_id=repo_member.members[0].user_id)

        viewmodel = GetProjectViewmodel(
            project=project).to_dict()

        expected = {
            'project': {
                'code': 'MF',
                'name': 'Maua Food',
                'description': 'É um aplicativo #foramoleza',
                'po_user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                'scrum_user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
                'start_date': 1634576165000,
                'members_user_ids': ['51ah5jaj-c9jm-1345-666ab-e12341c14a3','6f5g4h7J-876j-0098-123hb-hgb567fy4hb','93bc6ada-c0d1-7054-66ab-e17414c48ae3'],
                'photos': [
                    'https://i.imgur.com/gHoRKJU.png'
                ]
            },
            'message': 'the project was retrieved'
        }

        assert viewmodel == expected