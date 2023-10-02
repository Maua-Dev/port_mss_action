import pytest
from src.modules.update_action.app.update_action_usecase import UpdateActionUsecase
from src.modules.update_member.app.update_member_usecase import UpdateMemberUsecase
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_UpdateMemberUsecase:
    def test_update_member_usecase(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
#  ra: str, new_name: Optional[str] = None, new_email_dev: Optional[str] = None, new_email: Optional[str] = None, new_role: Optional[ROLE] = None, new_stack: Optional[STACK] = None, new_year: Optional[int] = None, new_cellphone: Optional[str] = None, new_course: Optional[COURSE] = None, new_hired_date: Optional[int] = None, new_deactivated_date: Optional[int] = None, new_active: Optional[ACTIVE] = None)

        member = usecase(     ra="21017310",new_name="Joao Branco",
                new_email_dev="jbranco.devmaua@gmail.com",
                new_email="jbranco@gmail.com",
             
                new_role=ROLE.HEAD,
                new_stack=STACK.BACKEND,
                new_year=3,
                new_cellphone="11991152348",
                new_course=COURSE.ECM,
                new_hired_date=1634921765000,
                new_active=ACTIVE.ACTIVE)
        
        assert repo.members[0] == member

    def test_update_member_no_items_found(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            member = usecase(ra="11111111",new_name="Joao Branco",
                new_email_dev="jbranco.devmaua@gmail.com",
                new_email="jbranco@gmail.com",
             
                new_role=ROLE.HEAD,
                new_stack=STACK.BACKEND,
                new_year=3,
                new_cellphone="11991152348",
                new_course=COURSE.ECM,
                new_hired_date=1634921765000,
                new_active=ACTIVE.ACTIVE)