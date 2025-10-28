from src.modules.delete_strike.app.delete_strike_controller import DeleteStrikeController
from src.modules.delete_strike.app.delete_strike_usecase import DeleteStrikeUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_DeleteStrikeController:
    def test_delete_strike_controller_success(self):
        repo = StrikeRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteStrikeUseCase(repo, repo_member)
        controller = DeleteStrikeController(usecase)

        strike_owner_id = repo.strikes[0].owner_user_id
        owner_member = next(m for m in repo_member.members if m.user_id == strike_owner_id)
        strike_to_delete_id = repo.strikes[0].strike_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": owner_member.user_id,
                "name": owner_member.name,
                "email": owner_member.email,
                "custom:isMaua": True
            },
            "strike_id": strike_to_delete_id
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == "the strike was deleted successfully"
        assert response.body["strike"]["strike_id"] == strike_to_delete_id
        assert response.body["strike"]["is_valid"] is True

    def test_delete_strike_controller_missing_requester_user(self):
        repo = StrikeRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteStrikeUseCase(repo, repo_member)
        controller = DeleteStrikeController(usecase)

        request = HttpRequest(body={
            "strike_id": repo.strikes[0].strike_id
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_delete_strike_controller_missing_strike_id(self):
        repo = StrikeRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteStrikeUseCase(repo, repo_member)
        controller = DeleteStrikeController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            }
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field strike_id is missing"

    def test_delete_strike_controller_invalid_strike_id(self):
        repo = StrikeRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteStrikeUseCase(repo, repo_member)
        controller = DeleteStrikeController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            "strike_id": "invalid_id"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field strike_id is not valid"

    def test_delete_strike_controller_not_found(self):
        repo = StrikeRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteStrikeUseCase(repo, repo_member)
        controller = DeleteStrikeController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            "strike_id": "263d81cc-6ba5-4853-a964-b2a368ab86bf"
        })

        response = controller(request)

        assert response.status_code == 404
        assert response.body == "No items found for strike_id"

    def test_delete_strike_controller_forbidden(self):
        repo = StrikeRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteStrikeUseCase(repo, repo_member)
        controller = DeleteStrikeController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[1].user_id,
                "name": repo_member.members[1].name,
                "email": repo_member.members[1].email,
                "custom:isMaua": True
            },
            "strike_id": repo.strikes[0].strike_id
        })

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "That action is forbidden for this type of user"