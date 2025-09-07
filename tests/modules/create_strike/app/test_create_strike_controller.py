from src.modules.create_strike.app.create_strike_controller import CreateStrikeController
from src.modules.create_strike.app.create_strike_usecase import CreateStrikeUsecase
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock


class Test_CreateStrikeController:

    def test_create_strike_controller_case_0(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'requester_user' : {
                "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "name": "Ryuske",
                "email": "ryuske@gmail.com",
                "custom:isMaua": True
            }, 
            'owner_user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            'target_user_id': "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0", 
            'occurred_date': 1725512986000,
            'category': 'OTHER',
            'description': "testing creating a strike"
        })
        response= controller(request=request)   

        assert response.status_code == 201
        assert response.body['owner_user_id'] == "51ah5jaj-c9jm-1345-666ab-e12341c14a3"
        assert response.body['target_user_id'] == "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0"
        assert response.body['applier_user_id'] == "3b07232f-4f65-42c6-b005-242550b8b8bf"
        assert response.body['occurred_date'] == 1725512986000
        assert response.body['category'] == 'OTHER'
        assert response.body['description'] == "testing creating a strike"
        assert response.body['message'] == "Strike was created successfully"
    
    def test_create_strike_controller_case_1(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'requester_user' : {
                "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "name": "Ryuske",
                "email": "ryuske@gmail.com",
                "custom:isMaua": True
            },
            'owner_user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            'target_user_id': "7gh5yf5H-857H-1234-75hng-94832hvng1s", 
            'occurred_date': 1757073600000,
            'category': 'OTHER',
            'description': "testing creating a strike"
        })

        response= controller(request=request)

        assert response.status_code == 201
        assert response.body['owner_user_id'] == "51ah5jaj-c9jm-1345-666ab-e12341c14a3"
        assert response.body['target_user_id'] == "7gh5yf5H-857H-1234-75hng-94832hvng1s"
        assert response.body['applier_user_id'] == "3b07232f-4f65-42c6-b005-242550b8b8bf"
        assert response.body['occurred_date'] == 1757073600000
        assert response.body['category'] == 'OTHER'
        assert response.body['description'] == "testing creating a strike"
        assert response.body['message'] == "Strike was created successfully and hours were reset"

    def test_create_strike_controller_requester_user_is_missing(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'owner_user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            'target_user_id': "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0", 
            'occurred_date': 1725512986000,
            'category': STRIKE_CATEGORY.OTHER,
            'description': "testing creating a strike"
        })
        response= controller(request=request)   

        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'

    def test_create_strike_controller_owner_user_id_is_missing(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'requester_user' : {
                "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "name": "Ryuske",
                "email": "ryuske@gmail.com",
                "custom:isMaua": True
            },
            'target_user_id': "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
            'occurred_date': 1725512986000,
            'category': STRIKE_CATEGORY.OTHER,
            'description': "testing creating a strike"
        })
        response= controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field owner_user_id is missing'

    def test_create_strike_controller_target_user_id_is_missing(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'requester_user' : {
                "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "name": "Ryuske",
                "email": "ryuske@gmail.com",
                "custom:isMaua": True
            },
            'owner_user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            'occurred_date': 1725512986000,
            'category': STRIKE_CATEGORY.OTHER,
            'description': "testing creating a strike"
        })

        response= controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field target_user_id is missing'

    def test_create_strike_controller_occurred_date_is_missing(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'requester_user' : {
                "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "name": "Ryuske",
                "email": "ryuske@gmail.com",
                "custom:isMaua": True
            },
            'owner_user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            'target_user_id': "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
            'category': STRIKE_CATEGORY.OTHER,
            'description': "testing creating a strike"
        })

        response= controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field occurred_date is missing'

    def test_create_strike_controller_category_is_missing(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'requester_user' : {
                "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "name": "Ryuske",
                "email": "ryuske@gmail.com",
                "custom:isMaua": True
            },
            'owner_user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            'target_user_id': "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
            'occurred_date': 1725512986000,
            'description': "testing creating a strike"
        })

        response= controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field category is missing'

    def test_create_strike_controller_owner_user_id_wrong_type(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'requester_user' : {
                "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "name": "Ryuske",
                "email": "ryuske@gmail.com",
                "custom:isMaua": True
            },
            'owner_user_id': 12345,
            'target_user_id': "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
            'occurred_date': 1725512986000,
            'category': STRIKE_CATEGORY.OTHER,
            'description': "testing creating a strike"
        })

        response= controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field owner_user_id isn't in the right type.\n Received: int.\n Expected: str"

    def test_create_strike_controller_target_user_id_wrong_type(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'requester_user' : {
                "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "name": "Ryuske",
                "email": "ryuske@gmail.com",
                "custom:isMaua": True
            },
            'owner_user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            'target_user_id': 12345,
            'occurred_date': 1725512986000,
            'category': STRIKE_CATEGORY.OTHER,
            'description': "testing creating a strike"
        })

        response= controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field target_user_id isn't in the right type.\n Received: int.\n Expected: str"

    def test_create_strike_controller_category_wrong_type(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'requester_user' : {
                "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "name": "Ryuske",
                "email": "ryuske@gmail.com",
                "custom:isMaua": True
            },
            'owner_user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            'target_user_id': "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
            'occurred_date': 1725512986000,
            'category': STRIKE_CATEGORY.OTHER,
            'description': "testing creating a strike"
        })

        response= controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field category is not valid"

    def test_create_strike_controller_description_wrong_type(self):
        repo= StrikeRepositoryMock()
        repo_member= MemberRepositoryMock()
        repo_action= ActionRepositoryMock()
        usecase= CreateStrikeUsecase(repo=repo, repo_member=repo_member, repo_action=repo_action)
        controller= CreateStrikeController(usecase=usecase)

        request= HttpRequest(body = {
            'requester_user' : {
                "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "name": "Ryuske",
                "email": "ryuske@gmail.com",
                "custom:isMaua": True
            },
            'owner_user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            'target_user_id': "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
            'occurred_date': 1725512986000,
            'category': 'OTHER',
            'description': 12345
        })

        response= controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field description isn't in the right type.\n Received: int.\n Expected: str"