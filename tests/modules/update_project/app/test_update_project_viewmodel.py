from src.modules.update_project.app.update_project_viewmodel import UpdateProjectViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class TestUpdateProjectViewmodel:
    def test_update_project_viewmodel(self):
        repo = ActionRepositoryMock()
        viewmodel = UpdateProjectViewmodel(repo.projects[1])

        expected = {
            'message': 'the project was updated',
            'project': {
                'code': 'PT',
                'name': 'Portfólio',
                'description': 'É um site',
                'po_user_id': '6f5g4h7J-876j-0098-123hb-hgb567fy4hb',
                'scrum_user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
                'start_date': 1673535600000,
                'photos': ['https://i.imgur.com/gHoRKJU.png'],
                'members_user_ids': [
                    '51ah5jaj-c9jm-1345-666ab-e12341c14a3','6f5g4h7J-876j-0098-123hb-hgb567fy4hb',  '93bc6ada-c0d1-7054-66ab-e17414c48ae3'
                ]
            }
        }

        assert viewmodel.to_dict() == expected