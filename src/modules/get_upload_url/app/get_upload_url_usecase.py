from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, ForbiddenAction
from src.shared.infra.repositories.S3Manager import S3Manager

class GetUploadUrlUsecase:
    def __init__(self, member_repo: IMemberRepository, s3_manager: S3Manager):
        self.member_repo = member_repo
        self.s3_manager = s3_manager

    def __call__(self, user_id: str, file_name: str) -> str:
        if not Member.validate_user_id(user_id):
            raise EntityError('user_id')

        requester = self.member_repo.get_member(user_id=user_id)
        if requester is None:
            raise UnregisteredUser()

        if not Member.validate_role_admin(role=requester.role):
            raise ForbiddenAction('requester user as he is neither Director nor Head')

        key = f"documents/{file_name}"

        url = self.s3_manager.generate_presigned_url(key=key)
        return url