from src.modules.portfolio_export_members.app.portfolio_export_members_usecase import PortfolioExportMembersUsecase
from src.modules.portfolio_export_members.app.portfolio_export_members_viewmodel import PortfolioExportMembersViewModel
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.active_enum import ACTIVE


class Test_PortfolioExportMembersViewModel:
    def test_portfolio_export_members_viewmodel(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = PortfolioExportMembersUsecase(member_repo, action_repo)

        members = usecase()
        viewmodel = PortfolioExportMembersViewModel(members=members).to_dict()

        assert 'homeCarousel' in viewmodel
        assert 'quoteCarousel' in viewmodel
        assert 'memberCarousel' in viewmodel

        first_home = viewmodel['homeCarousel'][0]
        assert 'name' in first_home
        assert 'photoPath' in first_home
        assert 'area' in first_home

    def test_portfolio_export_members_viewmodel_empty_list(self):
        viewmodel = PortfolioExportMembersViewModel(members=[]).to_dict()

        assert 'homeCarousel' in viewmodel
        assert 'quoteCarousel' in viewmodel
        assert 'memberCarousel' in viewmodel

        assert len(viewmodel['homeCarousel']) == 0
        assert len(viewmodel['quoteCarousel']) == 0
        assert len(viewmodel['memberCarousel']) == 0
        assert len(viewmodel.keys()) == 3

    def test_portfolio_export_members_viewmodel_carousels_same_length(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        members = PortfolioExportMembersUsecase(member_repo, action_repo)()
        viewmodel = PortfolioExportMembersViewModel(members=members).to_dict()

        assert len(viewmodel['homeCarousel']) == len(members)
        assert len(viewmodel['quoteCarousel']) == len(members)
        assert len(viewmodel['memberCarousel']) == len(members)

    def test_portfolio_export_members_viewmodel_home_carousel_keys_and_values(self):
        member_repo = MemberRepositoryMock()
        members = member_repo.members
        viewmodel = PortfolioExportMembersViewModel(members=members).to_dict()

        first_member = members[0]
        first_home = viewmodel['homeCarousel'][0]

        assert set(first_home.keys()) == {'name', 'photoPath', 'area'}
        assert first_home['name'] == first_member.name
        assert first_home['photoPath'] == first_member.photo
        assert first_home['area'] == first_member.stack.value

    def test_portfolio_export_members_viewmodel_quote_carousel_keys_and_values(self):
        member_repo = MemberRepositoryMock()
        members = member_repo.members
        viewmodel = PortfolioExportMembersViewModel(members=members).to_dict()

        first_member = members[0]
        first_quote = viewmodel['quoteCarousel'][0]

        assert set(first_quote.keys()) == {'name', 'quote', 'photoPath', 'role'}
        assert first_quote['name'] == first_member.name
        assert first_quote['photoPath'] == first_member.photo
        assert first_quote['role'] == first_member.role.value
        assert first_quote['quote'] == ""

    def test_portfolio_export_members_viewmodel_member_carousel_keys_and_values(self):
        member_repo = MemberRepositoryMock()
        members = member_repo.members
        viewmodel = PortfolioExportMembersViewModel(members=members).to_dict()

        first_member = members[0]
        first_carousel_member = viewmodel['memberCarousel'][0]

        assert set(first_carousel_member.keys()) == {'name', 'photoPath', 'email', 'role', 'phone'}
        assert first_carousel_member['name'] == first_member.name
        assert first_carousel_member['photoPath'] == first_member.photo
        assert first_carousel_member['email'] == first_member.email
        assert first_carousel_member['role'] == first_member.role.value
        assert first_carousel_member['phone'] == ""

    def test_portfolio_export_members_viewmodel_with_photo_and_quote(self):
        member = Member(
            name="Test Member",
            email_dev="testmember.devmaua@gmail.com",
            email="test@gmail.com",
            ra="21000000",
            role=ROLE.DEV,
            stack=STACK.FRONTEND,
            year=2,
            cellphone="11999999999",
            course=COURSE.ECM,
            hired_date=1634576165000,
            active=ACTIVE.ACTIVE,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            photo="https://i.imgur.com/photo.png"
        )
        member.quote = "Hello portfolio"

        viewmodel = PortfolioExportMembersViewModel(members=[member]).to_dict()

        assert viewmodel['homeCarousel'][0]['photoPath'] == "https://i.imgur.com/photo.png"
        assert viewmodel['homeCarousel'][0]['area'] == "FRONTEND"
        assert viewmodel['quoteCarousel'][0]['quote'] == "Hello portfolio"
        assert viewmodel['quoteCarousel'][0]['role'] == "DEV"
        assert viewmodel['memberCarousel'][0]['email'] == "test@gmail.com"
