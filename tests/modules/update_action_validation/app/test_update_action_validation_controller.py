from src.modules.update_action_validation.app.update_action_validation_controller import UpdateActionValidationController
from src.modules.update_action_validation.app.update_action_validation_usecase import UpdateActionValidationUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class TestUpdateActionValidationController:

    def test_update_action_validation_controller(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        use_case = UpdateActionValidationUsecase(repo_action, repo_member)
        controller = UpdateActionValidationController(use_case)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            "action_id": repo_action.actions[0].action_id,
            "is_valid": False
        }
        )

        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == "Action validation was updated successfully"
        assert response.body["action"]["action_id"] == "5f4f13df-e7d3-4a10-9219-197ceae9e3f0"
        assert response.body["action"]["is_valid"] == False
        assert response.body["action"]["user_id"] == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"

    def test_update_action_validation_controller_missing_action_id(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        use_case = UpdateActionValidationUsecase(repo_action, repo_member)
        controller = UpdateActionValidationController(use_case)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            "is_valid": False
        }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field action_id is missing"


    def test_update_action_validation_controller_missing_is_valid(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        use_case = UpdateActionValidationUsecase(repo_action, repo_member)
        controller = UpdateActionValidationController(use_case)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            "action_id": repo_action.actions[0].action_id
        }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field is_valid is missing"


    def test_update_action_validation_controller_missing_requester_user(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        use_case = UpdateActionValidationUsecase(repo_action, repo_member)
        controller = UpdateActionValidationController(use_case)

        request = HttpRequest(body={
            "action_id": repo_action.actions[0].action_id,
            "is_valid": False
        }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"