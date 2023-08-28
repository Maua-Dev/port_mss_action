import pytest
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.repositories.action_repository_dynamo import ActionRepositoryDynamo


class Test_ActionRepositoryDynamo:
    @pytest.mark.skip("Can't run test in github actions")
    def test_create_project(self):
        repo = ActionRepositoryDynamo()
        project = Project(code="MF",name="Maua Food",description="É um aplicativo #foramoleza",po_RA="21017310",scrum_RA="21010757",start_date=1634576165000,photos=["https://i.imgur.com/gHoRKJU.png"],members=["10017310","21010757","21017310"])
        resp = repo.create_project(project=project)
        
        assert resp == project
    
    @pytest.mark.skip("Can't run test in github actions")
    def test_create_action(self):
        repo = ActionRepositoryDynamo()
        action = Action(owner_ra="19017310",action_id="eefe6db8-e03e-42c3-9fd2-1de796139501",story_id=497,associated_members_ra=["23017310","10017310","17033730"],stack_tags=[STACK.INTERNAL],action_type_tag=ACTION_TYPE.ARCHITECT,project_code="SM",title="Retrospective",description="Reunião de planning",start_date=1667256000000,end_date=1690046000000,duration=22790000000)
        resp = repo.create_action(action=action)
        
        assert resp == action
    
    @pytest.mark.skip("Can't run test in github actions")
    def test_create_associated_action(self):
        repo = ActionRepositoryDynamo()
        associatedAction = AssociatedAction(member_ra="10017310",action_id="eefe6db8-e03e-42c3-9fd2-1de796139501",start_date=1667256000000)
        resp = repo.create_associated_action(associated_action=associatedAction)
        
        assert resp == associatedAction
        
    @pytest.mark.skip("Can't run test in github actions")
    def test_create_member(self):
        repo = ActionRepositoryDynamo()
        member = Member(name="Joao Branco",email_dev="jbranco.devmaua@gmail.com",email="jbranco@gmail.com",ra="21010757",role=ROLE.HEAD,stack=STACK.BACKEND,year=3,cellphone="11991152348",course=COURSE.ECM,hired_date=1634921765000,active=ACTIVE.ACTIVE)
        
        resp = repo.create_member(member=member)
        
        assert resp == member
        
    @pytest.mark.skip("Can't run test in github actions")
    def test_get_action(self):
        repo = ActionRepositoryDynamo()
        resp = repo.get_action(action_id="42e01f11-283c-4925-b0aa-e80ac6c1815a")
        
        assert resp