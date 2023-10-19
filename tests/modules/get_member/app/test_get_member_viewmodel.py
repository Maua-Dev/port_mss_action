from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.modules.get_member.app.get_member_viewmodel import GetMemberViewModel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class Test_GetMemberViewModel:
    def test_get_member_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)
        member = usecase(ra='21017310')

        viewmodel = GetMemberViewModel(
            member=member).to_dict()

        expected = {
            'member':{
                'name': 'Vitor Guirão MPNTM',
                    'email_dev': 'vsoller.devmaua@gmail.com',
                    'email': 'vsoller@airubio.com',
                    'ra': '21017310',
                    'role': 'DIRECTOR',
                    'stack': 'INFRA',
                    'year': 1,
                    'cellphone': '11991758098',
                    'course': 'ECA',
                    'hired_date': 1634576165000,
                    'deactivated_date': None,
                    'active': 'ACTIVE',
                    'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
            },
            "message" : "the member was retrieved"
        }

        assert viewmodel == expected