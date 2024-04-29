from src.modules.delete_action.app.delete_action_controller import DeleteActionController
from src.modules.delete_action.app.delete_action_usecase import DeleteActionUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_DeleteActionController:
    def test_deete_action_controller(self):
            repo = ActionRepositoryMock()
            repo_member = MemberRepositoryMock()
            usecase = DeleteActionUsecase(repo, repo_member)
            controller = DeleteActionController(usecase)
            request = HttpRequest(body={
                "requester_user": {
                    "sub": repo_member.members[3].user_id,
                    "name": repo_member.members[3].name,
                    "email": repo_member.members[3].email,
                    "custom:isMaua": True
                },
                "action_id": repo.actions[0].action_id
            })
            response = controller(request)
            assert response.status_code == 200
            assert response.body["message"] == "the action was deleted for all the members in this action"
            assert response.body["action"]["user_id"] == "6f5g4h7J-876j-0098-123hb-hgb567fy4hb"
            assert response.body["action"]["story_id"] == 94
            assert response.body["action"]["is_valid"] == True
            assert response.body["action"]["associated_members_user_ids"] == ["75648hbr-184n-1985-91han-7ghn4HgF182", "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4", "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "6574hgyt-785n-9134-18gn4-7gh5uvn36cG", "7gh5yf5H-857H-1234-75hng-94832hvng1s"]
            assert response.body["action"]["stack_tags"] == ['INFRA']
            assert response.body["action"]["action_type_tag"] == "CODEREVIEW"
            assert response.body["action"]["project_code"] == "PT"
            assert response.body["action"]["title"] == "Retrospectiva"
            assert response.body["action"]["description"] == "Revisão de sprint"
            assert response.body["action"]["start_date"] == 1644256000000
            assert response.body["action"]["end_date"] == 1653756000000
            assert response.body["action"]["duration"] == 9500000000

    def test_delete_action_controller_missing_action_id(self):
            repo = ActionRepositoryMock()
            repo_member = MemberRepositoryMock()
            usecase = DeleteActionUsecase(repo, repo_member)
            controller = DeleteActionController(usecase)
            request = HttpRequest(body={
                "requester_user": {
                    "sub": repo_member.members[3].user_id,
                    "name": repo_member.members[3].name,
                    "email": repo_member.members[3].email,
                    "custom:isMaua": True
                },
            })
            response = controller(request)
            assert response.status_code == 400
            assert response.body == "Field action_id is missing"

    def test_delete_action_controller_invalid_action_id(self):
            repo = ActionRepositoryMock()
            repo_member = MemberRepositoryMock()
            usecase = DeleteActionUsecase(repo, repo_member)
            controller = DeleteActionController(usecase)
            request = HttpRequest(body={
                "requester_user": {
                    "sub": repo_member.members[3].user_id,
                    "name": repo_member.members[3].name,
                    "email": repo_member.members[3].email,
                    "custom:isMaua": True
                },
                "action_id": "invalid_id"
            })
            response = controller(request)
            assert response.status_code == 400
            assert response.body == "Field action_id is not valid"

    def test_delete_action_controller_missing_requester_user(self):
            repo = ActionRepositoryMock()
            repo_member = MemberRepositoryMock()
            usecase = DeleteActionUsecase(repo, repo_member)
            controller = DeleteActionController(usecase)
            request = HttpRequest(body={
                "action_id": repo.actions[0].action_id
            })
            response = controller(request)
            assert response.status_code == 400
            assert response.body == "Field requester_user is missing"
