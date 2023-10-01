
import pytest
from src.modules.create_action.app.create_action_usecase import CreateActionUsecase
from src.modules.create_member.app.create_member_usecase import CreateMemberUsecase
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_CreateMemberUsecase:
    def test_create_member_usecase(self):
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        lenBefore = len(repo.members)
        
        member = usecase(         
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1614567601000,
            deactivated_date=None
            )
        
        assert len(repo.members) == lenBefore + 1
        assert repo.members[-1] == member
    