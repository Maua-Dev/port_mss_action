
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
        
        
        member = usecase(         
            name="VitOr GUIrão MpNTm",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="18563125",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            user_id="75638hbr-184n-1985-91han-7ghn4HgF182"
            )
        
        assert repo.members[-1] == member
        assert member.name == "Vitor Guirão Mpntm"
        
    def test_create_member_usecase_duplicated_user_id(self):
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        
        
        with pytest.raises(DuplicatedItem):
            member = usecase(         
            name="Vitor Guirão Mpntm",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3"
            )
        
        
    