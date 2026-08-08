from src.modules.create_strike.app.create_strike_usecase import CreateStrikeUsecase
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, UnregisteredUser, UserIsNotFromAdmin, UserIsNotFromRH, MemberAlreadyReachedStrikeLimit
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock
import pytest

class Test_CreateStrikeUsecase:
    def test_create_strike_usecase_user_has_less_than_3_strikes(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)

        returned_strike=usecase(
            owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            target_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0", 
            applier_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            occurred_date=1725512986000,
            category=STRIKE_CATEGORY.OTHER,
            description="testing creating a strike"
        )

        assert returned_strike[1] == 0
        assert returned_strike[0].owner_user_id == "51ah5jaj-c9jm-1345-666ab-e12341c14a3"
        assert returned_strike[0].target_user_id == "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0"
        assert returned_strike[0].applier_user_id == "51ah5jaj-c9jm-1345-666ab-e12341c14a3"
    
    def test_create_strike_usecase_user_has_4_strikes_and_is_in_4_projects(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)

        with pytest.raises(MemberAlreadyReachedStrikeLimit):
            returned_strike= usecase(
                owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                target_user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s", 
                applier_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                occurred_date=1764622800000,
                category=STRIKE_CATEGORY.OTHER,
                description="testing creating a strike"
            )

    def test_create_strike_usecase_user_has_3_strikes_and_is_in_4_projects(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        
        # Remove one strike to make it exactly 3 strikes before the request
        repo.delete_strike("i9j0k1l2-m3n4-5678-9012-345678ijklmn")
        
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)

        returned_strike= usecase(
            owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            target_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb", 
            applier_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            occurred_date=1764622800000,
            category=STRIKE_CATEGORY.OTHER,
            description="testing creating a strike"
        )

        assert returned_strike[1] == 1
        assert returned_strike[0].owner_user_id == "51ah5jaj-c9jm-1345-666ab-e12341c14a3"
        assert returned_strike[0].target_user_id == "6f5g4h7J-876j-0098-123hb-hgb567fy4hb"
        assert returned_strike[0].applier_user_id == "51ah5jaj-c9jm-1345-666ab-e12341c14a3"
        assert repo_action.get_action_durations_for_user(user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3", start_date=1764558000000, end_date=1782874740000) == 0

    def test_create_strike_usecase_user_has_5_strikes_and_is_in_3_projects(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)

        with pytest.raises(MemberAlreadyReachedStrikeLimit):
            returned_strike= usecase(
                owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                target_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb", 
                applier_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                occurred_date=1764622800000,
                category=STRIKE_CATEGORY.OTHER,
                description="testing creating a strike"
            )

    def test_create_strike_usecase_target_user_is_not_registered(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)

        with pytest.raises(UnregisteredUser):
            returned_strike= usecase(
                owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                target_user_id="7gh5yf5H-857H-1234-75hng-94832hvnh5e", 
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1757073600000,
                category=STRIKE_CATEGORY.OTHER,
                description="testing creating a strike"
            )

    def test_create_strike_target_user_is_not_active(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)

        with pytest.raises(ForbiddenAction):
            returned_strike= usecase(
                owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                target_user_id="76h35dg4-h76v-1875-987hn-h67gfv45Gt4", 
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1757073600000,
                category=STRIKE_CATEGORY.OTHER,
                description="testing creating a strike"
            )

    def test_create_strike_ower_user_is_not_director(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)

        with pytest.raises(ForbiddenAction):
            returned_strike= usecase(
                owner_user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s",
                target_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0", 
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1757073600000,
                category=STRIKE_CATEGORY.OTHER,
                description="testing creating a strike"
            )

    def test_create_strike_applier_user_is_not_director(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)

        with pytest.raises(ForbiddenAction):
            returned_strike= usecase(
                owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                target_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0", 
                applier_user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s",
                occurred_date=1757073600000,
                category=STRIKE_CATEGORY.OTHER,
                description="testing creating a strike"
            )
    
    def test_create_strike_applier_user_is_internal_but_not_from_rh(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)

        with pytest.raises(ForbiddenAction) as e:
            returned_strike= usecase(
                owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                target_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0", 
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8h9ir",
                occurred_date=1757073600000,
                category=STRIKE_CATEGORY.OTHER,
                description="testing creating a strike"
            )

    def test_create_strike_applier_user_is_not_active(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)

        with pytest.raises(ForbiddenAction):
            returned_strike= usecase(
                owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                target_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0", 
                applier_user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                occurred_date=1757073600000,
                category=STRIKE_CATEGORY.OTHER,
                description="testing creating a strike"
            )
    
