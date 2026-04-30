from unittest.mock import MagicMock
from src.modules.get_upload_url.app.get_upload_url_controller import GetUploadUrlController
from src.modules.get_upload_url.app.get_upload_url_usecase import GetUploadUrlUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden

class Test_GetUploadUrlController:
    def test_get_upload_url_controller(self):
        repo = MemberRepositoryMock()
        s3_manager = MagicMock()
        s3_manager.generate_presigned_url.return_value = "https://mocked-url.com"
        usecase = GetUploadUrlUsecase(repo, s3_manager)
        controller = GetUploadUrlController(usecase)
        
        request = HttpRequest(body={
            "requester_user": {
                "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller.devmaua@gmail.com",
                "custom:isMaua": "true"
            },
            "file_name": "doc.pdf"
        })
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body["upload_url"] == "https://mocked-url.com"
        assert response.body["message"] == "presigned url generated successfully"

    def test_get_upload_url_controller_missing_requester_user(self):
        repo = MemberRepositoryMock()
        s3_manager = MagicMock()
        usecase = GetUploadUrlUsecase(repo, s3_manager)
        controller = GetUploadUrlController(usecase)
        
        request = HttpRequest(body={
            "file_name": "doc.pdf"
        })
        
        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_get_upload_url_controller_missing_file_name(self):
        repo = MemberRepositoryMock()
        s3_manager = MagicMock()
        usecase = GetUploadUrlUsecase(repo, s3_manager)
        controller = GetUploadUrlController(usecase)
        
        request = HttpRequest(body={
            "requester_user": {
                "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller.devmaua@gmail.com",
                "custom:isMaua": "true"
            }
        })
        
        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == "Field file_name is missing"
        
    def test_get_upload_url_controller_forbidden_action(self):
        repo = MemberRepositoryMock()
        s3_manager = MagicMock()
        usecase = GetUploadUrlUsecase(repo, s3_manager)
        controller = GetUploadUrlController(usecase)
        
        request = HttpRequest(body={
            "requester_user": {
                "sub": "76h35dg4-h76v-1875-987hn-h67gfv45Gt4",
                "name": "Luigi Televisão",
                "email": "ltelevisao.devmaua@gmail.com",
                "custom:isMaua": "true"
            },
            "file_name": "doc.pdf"
        })
        
        response = controller(request)
        
        assert response.status_code == 403
        assert response.body == "That action is forbidden for this requester user as he is neither Director nor Head"
