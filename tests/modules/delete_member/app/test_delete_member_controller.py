from src.modules.delete_member.app.delete_member_controller import DeleteMemberController
from src.modules.delete_member.app.delete_member_usecase import DeleteMemberUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_DeleteMemberController:
    def test_delete_member_controller(self):
        
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        controller = DeleteMemberController(usecase=usecase)
        member = repo.members[0]
        request = HttpRequest(
            headers={
                'requester_user': {
                    "sub": member.user_id,
                    "name": member.name,
                    "email": member.email,
                    "custom:isMaua": True
                }
            }
        )

        response = controller(request)
        assert response.status_code == 200
        assert response.body["member"]["name"] == "Vitor Guirão MPNTM"
        assert response.body["member"]["email_dev"] == "vsoller.devmaua@gmail.com"
        assert response.body["member"]["email"] == "vsoller@airubio.com"
        assert response.body["member"]["ra"] == "21017310"
        assert response.body["member"]["role"] == "DIRECTOR"
        assert response.body["member"]["stack"] == "INFRA"
        assert response.body["member"]["year"] == 1
        assert response.body["member"]["cellphone"] == "11991758098"
        assert response.body["member"]["course"] == "ECA"
        assert response.body["member"]["hired_date"] == 1634576165000
        assert response.body["member"]["active"] == "ACTIVE"
        assert response.body["member"]["user_id"] == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        
    def test_delete_controller_invalid_id(self):
            
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        controller = DeleteMemberController(usecase=usecase)
        member = repo.members[0]
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": 666,
                    "name": member.name,
                    "email": member.email,
                    "custom:isMaua": True
                }
            }
        )
        
        response = controller(request=request)

        assert response.status_code == 400
        
    def test_delete_controller_user_id_none(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        controller = DeleteMemberController(usecase=usecase)
        member = repo.members[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": None,
                    "name": member.name,
                    "email": member.email,
                    "custom:isMaua": True
                }
            }
        )

        response = controller(request=request)

        assert response.status_code == 400

    def test_delete_controller_user_id_not_found(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        controller = DeleteMemberController(usecase=usecase)
        member = repo.members[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "name": member.name,
                    "email": member.email,
                    "custom:isMaua": True
                }
            }
        )

        response = controller(request=request)

        assert response.status_code == 404
        
    