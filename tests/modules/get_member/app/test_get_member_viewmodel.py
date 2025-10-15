from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.modules.get_member.app.get_member_viewmodel import GetMemberViewModel
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock  
from pprint import pprint 

class Test_GetMemberViewModel:
    def test_get_member_viewmodel(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        strike_repo = StrikeRepositoryMock()
        usecase = GetMemberUsecase(member_repo, action_repo, strike_repo)
        member = usecase(user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', start_date= 1624576165000, end_date= 1690046000000)

        viewmodel = GetMemberViewModel(
            member=member).to_dict()
        
        pprint(viewmodel)

        expected = {'member': {'active': 'ACTIVE',
            'cellphone': '11991758098',
            'course': 'ECA',
            'deactivated_date': None,
            'email': 'vsoller@airubio.com',
            'email_dev': 'vsoller.devmaua@gmail.com',
            'hired_date': 1634576165000,
            'hours_worked': 134460000000,
            'name': 'Vitor Guirão MPNTM',
            'photo': None,
            'project': ['Maua Food', 'Portfólio', 'Selfie Mauá'],
            'ra': '21017310',
            'role': 'DIRECTOR',
            'stack': 'INFRA',
            'strikes': 0,
            'strikes_allowed': 4,
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'year': 1},
 'message': 'the member was retrieved'}
        
        assert viewmodel == expected
        