from src.modules.get_member_info.app.get_member_info_usecase import GetMemberInfoUsecase
from src.modules.get_member_info.app.get_member_info_viewmodel import GetMemberInfoViewModel
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from pprint import pprint


class Test_GetMemberInfoViewModel:
    def test_get_member_info_viewmodel(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = GetMemberInfoUsecase(member_repo, action_repo)

        # Primeiro membro: Vitor Guirão
        member = usecase(user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3')
        viewmodel = GetMemberInfoViewModel(member=member).to_dict()

        pprint(viewmodel)

        expected = {
            'member_info': {
                'name': 'Vitor Guirão MPNTM',
                'ra': '21017310',
                'role': 'DIRECTOR',
                'stack': 'INFRA',
                'year': 1,
                'course': 'ECA',
                'project': ['Maua Food', 'Portfólio', 'Selfie Mauá'],
                'hired_date': 1634576165000,
                'photo': None
            },
            'message': 'the member info was retrieved successfully'
        }

        assert viewmodel == expected

    def test_get_member_info_viewmodel_another_member(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = GetMemberInfoUsecase(member_repo, action_repo)

        # Little Ronald - DIRECTOR, FRONTEND
        member = usecase(user_id='6f5g4h7J-876j-0098-123hb-hgb567fy4hb')
        viewmodel = GetMemberInfoViewModel(member=member).to_dict()

        pprint(viewmodel)

        assert 'member_info' in viewmodel
        assert viewmodel['member_info']['name'] == 'Little Ronald'
        assert viewmodel['member_info']['ra'] == '10017310'
        assert viewmodel['member_info']['role'] == 'DIRECTOR'
        assert viewmodel['member_info']['stack'] == 'FRONTEND'
        assert viewmodel['member_info']['year'] == 6
        assert viewmodel['member_info']['course'] == 'ECM'
        assert viewmodel['member_info']['project'] == ['Maua Food', 'Portfólio', 'Selfie Mauá', 'SMILE']
        assert viewmodel['member_info']['hired_date'] == 1614567601000
        assert viewmodel['member_info']['photo'] is None