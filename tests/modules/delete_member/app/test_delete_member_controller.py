from src.modules.delete_member.app.delete_member_controller import DeleteMemberController
from src.modules.delete_member.app.delete_member_usecase import DeleteMemberUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_DeleteMemberController:
    def test_delete_member_controller(self):
        
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo)
        controller = DeleteMemberController(usecase)
        request = HttpRequest(body={
            'ra': '21017310'
        })
        response = controller(request)
        assert response.status_code == 200
        assert response.body["message"] == "the member was deleted"
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
        
        
        
        
    def test_delete_member_controller_missing_ra(self):
        
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo)
        controller = DeleteMemberController(usecase)
        request = HttpRequest(body={})
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field ra is missing"
        
    def test_delete_member_controller_invalid_ra(self): 
            
            repo = MemberRepositoryMock()
            usecase = DeleteMemberUseCase(repo)
            controller = DeleteMemberController(usecase)
            request = HttpRequest(body={
                'ra': '2000822843'
            })
            response = controller(request)
            assert response.status_code == 400
            assert response.body == "Field ra is not valid"
            
    def test_delete_member_controller_member_not_found(self):
                
                repo = MemberRepositoryMock()
                usecase = DeleteMemberUseCase(repo)
                controller = DeleteMemberController(usecase)
                request = HttpRequest(body={
                    'ra': '20008228'
                })
                response = controller(request)
                assert response.status_code == 404
                assert response.body == "No items found for member"