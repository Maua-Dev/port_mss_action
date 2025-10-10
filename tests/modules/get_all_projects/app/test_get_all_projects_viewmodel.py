from src.modules.get_all_projects.app.get_all_projects_usecase import GetAllProjectsUsecase
from src.modules.get_all_projects.app.get_all_projects_viewmodel import GetAllProjectsViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from pprint import pprint


class Test_GetAllProjectsViewmodel:
    def test_get_all_projects_viewmodel(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetAllProjectsUsecase(repo, repo_member)
        projects = usecase(repo_member.members[0].user_id,1637046000000, 1690046000000)

        viewmodel = GetAllProjectsViewmodel(projects).to_dict()
        
        pprint(viewmodel)

        expected = {'message': 'the projects were retrieved',
 'projects': [{'project': {'code': 'MF',
                           'description': 'É um aplicativo #foramoleza',
                           'hours_worked': 62120000000,
                           'members_user_ids': ['51ah5jaj-c9jm-1345-666ab-e12341c14a3',
                                                '6f5g4h7J-876j-0098-123hb-hgb567fy4hb',
                                                '93bc6ada-c0d1-7054-66ab-e17414c48ae3'],
                           'name': 'Maua Food',
                           'photo': 'https://i.imgur.com/gHoRKJU.png',
                           'po_user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                           'scrum_user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
                           'start_date': 1634576165000}},
              {'project': {'code': 'PT',
                           'description': 'É um site',
                           'hours_worked': 0,
                           'members_user_ids': ['51ah5jaj-c9jm-1345-666ab-e12341c14a3',
                                                '6f5g4h7J-876j-0098-123hb-hgb567fy4hb',
                                                '93bc6ada-c0d1-7054-66ab-e17414c48ae3'],
                           'name': 'Portfólio',
                           'photo': 'https://i.imgur.com/gHoRKJU.png',
                           'po_user_id': '6f5g4h7J-876j-0098-123hb-hgb567fy4hb',
                           'scrum_user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
                           'start_date': 1673535600000}},
              {'project': {'code': 'SF',
                           'description': 'Aplicativo para reconhecimento '
                                          'facial',
                           'hours_worked': 96530000000,
                           'members_user_ids': ['51ah5jaj-c9jm-1345-666ab-e12341c14a3',
                                                '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
                                                '6f5g4h7J-876j-0098-123hb-hgb567fy4hb',
                                                '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                                                '93bc6ada-c0d1-7054-66ab-e17414c48ae3'],
                           'name': 'Selfie Mauá',
                           'photo': None,
                           'po_user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                           'scrum_user_id': '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
                           'start_date': 1686754800000}},
              {'project': {'code': 'SM',
                           'description': 'Site do evento SMILE',
                           'hours_worked': 47430000000,
                           'members_user_ids': ['51ah5jaj-c9jm-1345-666ab-e12341c14a3',
                                                '6f5g4h7J-876j-0098-123hb-hgb567fy4hb',
                                                '7465hvnb-143g-1675-86HnG-75hgnFbcg36',
                                                '7gh5yf5H-857H-1234-75hng-94832hvng1s'],
                           'name': 'SMILE',
                           'photo': None,
                           'po_user_id': '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                           'scrum_user_id': '7465hvnb-143g-1675-86HnG-75hgnFbcg36',
                           'start_date': 1639321200000}},
              {'project': {'code': 'GM',
                           'description': 'Projeto para organização dos '
                                          'membros do DEV',
                           'hours_worked': 1320000000,
                           'members_user_ids': ['76h35dg4-h76v-1875-987hn-h67gfv45Gt4',
                                                '7gh5yf5H-857H-1234-75hng-94832hvng1s'],
                           'name': 'Gameficação',
                           'photo': None,
                           'po_user_id': '76h35dg4-h76v-1875-987hn-h67gfv45Gt4',
                           'scrum_user_id': '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                           'start_date': 1672585200000}},
              {'project': {'code': 'HZ',
                           'description': 'Projeto de molde para zerar as '
                                          'horas',
                           'hours_worked': 0,
                           'members_user_ids': ['76h35dg4-h76v-1875-987hn-h67gfv45Gt4',
                                                '7gh5yf5H-857H-1234-75hng-94832hvng1s'],
                           'name': 'Zeragem de Horas',
                           'photo': None,
                           'po_user_id': '76h35dg4-h76v-1875-987hn-h67gfv45Gt4',
                           'scrum_user_id': '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                           'start_date': 1672585200000}}]}
        
        assert viewmodel == expected