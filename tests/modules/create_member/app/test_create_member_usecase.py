import datetime

import pytest
from src.modules.create_member.app.create_member_usecase import CreateMemberUsecase
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_CreateMemberUsecase:
    def test_create_member_usecase(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        lenBefore = len(repo.members)
        
        member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
        
        assert len(repo.members) == lenBefore + 1
        
        assert repo.members[-1].name == "Teste"
        assert repo.members[-1].email == "teste.devmaua@gmail.com"
        assert repo.members[-1].ra == "12345678"
        assert repo.members[-1].role == ROLE.DEV
        assert repo.members[-1].stack == STACK.BACKEND
        assert repo.members[-1].year == 2
        assert repo.members[-1].cellphone == "11912345678"
        assert repo.members[-1].course == COURSE.CIC
        assert repo.members[-1].hired_date == datetime.datetime(2021, 10, 18)
        assert repo.members[-1].active == ACTIVE.ACTIVE
        assert repo.members[-1].deactivated_date == datetime.datetime(2022, 10, 18)
        assert repo.members[-1].projects[0].code == "MF"
        assert repo.members[-1].projects[0].name == "Maua Food"
        assert repo.members[-1].projects[0].description == "É um aplicativo #foramoleza"
        
    def test_create_member_usecase_without_deactivated_date(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        lenBefore = len(repo.members)
        
        member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])

        assert len(repo.members) == lenBefore + 1
        assert repo.members[-1].deactivated_date == None
    
    def test_create_member_usecase_without_projects(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        lenBefore = len(repo.members)
        
        member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.FRONTEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18))
        
        assert len(repo.members) == lenBefore + 1
        assert repo.members[-1].projects == []
        
    def test_create_member_usecase_duplicated_member(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(DuplicatedItem):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="22017310", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18))
    
    def test_create_member_usecase_name_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name=None, email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18))
            
    def test_create_member_usecase_invalid_name_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name=True, email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18))
            
    def test_create_member_usecase_invalid_name_length(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="O", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18))

    def test_create_member_usecase_email_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email=None, ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
    
    def test_create_member_usecase_invalid_email_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email=1, ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18))
    
    def test_create_member_usecase_email_not_email(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="@.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18))
            
    def test_create_member_usecase_email_not_devmaua(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18))
            
    def test_create_member_usecase_ra_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra=None, role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_ra_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra=12345678, role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_ra(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="123", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_role_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=None, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_role_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role="DEV", stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_stack_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=None, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_stack_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack="BACKEND", year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_year_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=None, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_year_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year="2", cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_year(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2022, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_cellphone_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone=None, course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_cellphone_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone=11912345678, course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_cellphone_length(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_course_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=None, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_course_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course="CIC", hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_hired_date_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=None, active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_hired_date_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date="18-10-2021", active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_active_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=None, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_active_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=True, deactivated_date=datetime.datetime(2022, 10, 18), projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_deactivated_date(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date="18-10-2022", projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
            
    def test_create_member_usecase_invalid_project_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza"))
            
    def test_create_member_usecase_invalid_project_list_items_type(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE, deactivated_date=datetime.datetime(2022, 10, 18), projects=["MF", "PT"])