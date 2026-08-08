import pytest
from unittest.mock import MagicMock
from src.modules.get_upload_url.app.get_upload_url_usecase import GetUploadUrlUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, ForbiddenAction
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.S3Manager import S3Manager

class Test_GetUploadUrlUsecase:
    def test_get_upload_url_usecase(self):
        repo = MemberRepositoryMock()
        s3_manager = MagicMock() #Simula o s3 manager mas so de
        s3_manager.generate_presigned_url.return_value = "https://mocked-url.com"
        usecase = GetUploadUrlUsecase(repo, s3_manager)
        
        url = usecase("93bc6ada-c0d1-7054-66ab-e17414c48ae3", "doc.pdf")
        
        assert url == "https://mocked-url.com"
        s3_manager.generate_presigned_url.assert_called_once_with(key="documents/doc.pdf")


    def test_get_upload_url_usecase_real_s3(self):
        import os
        os.environ["STAGE"] = "TEST"
        repo = MemberRepositoryMock()
        
        s3_manager = S3Manager()
        usecase = GetUploadUrlUsecase(repo, s3_manager)
        
        url = usecase("93bc6ada-c0d1-7054-66ab-e17414c48ae3", "doc.pdf")
        
        assert url is not None
        assert type(url) == str

    def test_get_upload_url_usecase_invalid_user_id(self):
        repo = MemberRepositoryMock()
        s3_manager = S3Manager() 
        usecase = GetUploadUrlUsecase(repo, s3_manager)
        
        with pytest.raises(EntityError):
            usecase(123, "doc.pdf")

    def test_get_upload_url_usecase_unregistered_user(self):
        repo = MemberRepositoryMock()
        s3_manager = MagicMock()
        usecase = GetUploadUrlUsecase(repo, s3_manager)
        
        with pytest.raises(UnregisteredUser):
            usecase("99999999-9999-9999-9999-999999999999", "doc.pdf")

    def test_get_upload_url_usecase_forbidden_action(self):
        repo = MemberRepositoryMock()
        s3_manager = MagicMock()
        usecase = GetUploadUrlUsecase(repo, s3_manager)
        
        with pytest.raises(ForbiddenAction):
            usecase("76h35dg4-h76v-1875-987hn-h67gfv45Gt4", "doc.pdf")
