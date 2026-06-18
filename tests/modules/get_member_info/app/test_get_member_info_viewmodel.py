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

        members = usecase(requester_user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3')
        viewmodel = GetMemberInfoViewModel(members=members).to_dict()

        assert 'homeCarousel' in viewmodel
        assert 'quoteCarousel' in viewmodel
        assert 'memberCarousel' in viewmodel

        first_home = viewmodel['homeCarousel'][0]
        assert 'name' in first_home
        assert 'photoPath' in first_home
        assert 'area' in first_home

    def test_get_member_info_viewmodel_empty_list(self):
        viewmodel = GetMemberInfoViewModel(members=[]).to_dict()

        assert 'homeCarousel' in viewmodel
        assert 'quoteCarousel' in viewmodel
        assert 'memberCarousel' in viewmodel

        assert len(viewmodel['homeCarousel']) == 0
        assert len(viewmodel['quoteCarousel']) == 0
        assert len(viewmodel['memberCarousel']) == 0
        assert len(viewmodel.keys()) == 3