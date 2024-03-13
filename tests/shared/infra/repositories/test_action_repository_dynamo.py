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
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_ActionRepositoryDynamo:
    
    @pytest.mark.skip("Can't run test in github actions")
    def test_create_project(self):
        repo = ActionRepositoryDynamo()
        project = Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza", po_RA="21017310", scrum_RA="21010757",
                          start_date=1634576165000, photos=["https://i.imgur.com/gHoRKJU.png"], members=["10017310", "21010757", "21017310"],
                          members_user_ids=["148c6ada-c0d1-7054-66ab-e17414c48ae3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "148caada-c0d1-7054-66ab-e17414c48ae3"])
        resp = repo.create_project(project=project)

        assert resp == project

    @pytest.mark.skip("Can't run test in github actions")
    def test_create_action(self):
        repo = ActionRepositoryDynamo()
        action = Action(owner_ra="19017310", action_id="eefe6db8-e03e-42c3-9fd2-1de796139501", story_id=497, associated_members_user_ids=["148c6ada-c0d1-7054-66ab-e17414c48ae3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "148caada-c0d1-7054-66ab-e17414c48ae3"], stack_tags=[
                        STACK.INTERNAL], action_type_tag=ACTION_TYPE.ARCHITECT, project_code="SM", title="Retrospective", description="Reunião de planning", start_date=1667256000000, end_date=1690046000000, duration=22790000000,
                        user_id="148c6ada-c0d1-7054-66ab-e17414c48ae3", is_valid=True)
        resp = repo.create_action(action=action)

        assert resp == action

    @pytest.mark.skip("Can't run test in github actions")
    def test_create_associated_action(self):
        repo = ActionRepositoryDynamo()
        associatedAction = AssociatedAction(
            member_ra="10017310", action_id="eefe6db8-e03e-42c3-9fd2-1de796139501", start_date=1667256000000, user_id="148c6ada-c0d1-7054-66ab-e17414c48ae3")
        resp = repo.create_associated_action(
            associated_action=associatedAction)

        assert resp == associatedAction

    @pytest.mark.skip("Can't run test in github actions")
    def test_create_member(self):
        repo = ActionRepositoryDynamo()
        member = Member(name="Joao Branco", email_dev="jbranco.devmaua@gmail.com", email="jbranco@gmail.com", ra="21010757", role=ROLE.HEAD,
                        stack=STACK.BACKEND, year=3, cellphone="11991152348", course=COURSE.ECM, hired_date=1634921765000, active=ACTIVE.ACTIVE, user_id="75648hbr-184n-1985-91han-7ghn4HgF182")

        resp = repo.create_member(member=member)

        assert resp == member

    @pytest.mark.skip("Can't run test in github actions")
    def test_get_action(self):
        repo = ActionRepositoryDynamo()
        resp = repo.get_action(
            action_id="42e01f11-283c-4925-b0aa-e80ac6c1815a")

        expected = Action(owner_ra="10017310", action_id="42e01f11-283c-4925-b0aa-e80ac6c1815a", story_id=983, associated_members_ra=["21017310", "19017310", "19017311", "23017310", "17033730"], stack_tags=[
                          STACK.INFRA], action_type_tag=ACTION_TYPE.WORK, project_code="SF", title="Retrospectiva", description="Revisão de sprint", start_date=1641896000000, end_date=1679686000000, duration=37790000000,
                          user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb", is_valid=True)
        assert resp == expected

    @pytest.mark.skip("Can't run test in github actions")
    def test_get_all_projects(self):
        repo = ActionRepositoryDynamo()
        resp = repo.get_all_projects()

        assert resp == [Project(code="GM",name="Gameficação",description="Projeto para organização dos membros do DEV",po_RA="22084120",scrum_RA="22015940",start_date=1672585200000,members=["22015940","22084120"], members_user_ids=["76h35dg4-h76v-1875-987hn-h67gfv45Gt4", "7gh5yf5H-857H-1234-75hng-94832hvng1s"]), Project(code="MF",name="Maua Food",description="É um aplicativo #foramoleza",po_RA="21017310",scrum_RA="21010757",start_date=1634576165000,photos=["https://i.imgur.com/gHoRKJU.png"],members=["10017310","21010757","21017310"], members_user_ids=["6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]),Project(code="PT",name="Portfólio",description="É um site",po_RA="22011020",scrum_RA="21010757",start_date=1673535600000,photos=["https://i.imgur.com/gHoRKJU.png"],members=["10017310","21010757","22011020"], members_user_ids=["6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]),Project(code="SF",name="Selfie Mauá",description="Aplicativo para reconhecimento facial",po_RA="22931270",scrum_RA="21020532",start_date=1686754800000,members=["10017310","19017311","21010757","21020532","22931270"], members_user_ids=["6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "7gh5yf5H-857H-1234-75hng-94832hvng1s", "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "6574hgyt-785n-9134-18gn4-7gh5uvn36cG" ]),Project(code="SM",name="SMILE",description="Site do evento SMILE",po_RA="15014025",scrum_RA="21010757",start_date=1639321200000,members=["10017310","15014025","19017311","21010757"], members_user_ids=["6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "7465hvnb-143g-1675-86HnG-75hgnFbcg36", "7gh5yf5H-857H-1234-75hng-94832hvng1s", "51ah5jaj-c9jm-1345-666ab-e12341c14a3"])]

    @pytest.mark.skip("Can't run test in github actions")
    def test_delete_project(self):
        repo_dynamo = ActionRepositoryDynamo()
        repo_mock = ActionRepositoryMock()

        project = repo_mock.projects[0]

        delected_project= repo_dynamo.delete_project(project.code)

        assert delected_project == project

    @pytest.mark.skip("Can't run test in github actions")
    def test_get_all_members(self):
        repo = ActionRepositoryDynamo()
        repo_mock = ActionRepositoryMock()

        members = repo_mock.members

        resp = repo.get_all_members()

        members.sort(key=lambda x: x.ra)

        assert resp == members

    
    @pytest.mark.skip("Can't run test in github actions")
    def test_get_member(self):
        repo = ActionRepositoryDynamo()
        repo_mock = ActionRepositoryMock()

        member = repo_mock.members[0]

        resp = repo.get_member(member.ra)

        assert resp == member
    
    @pytest.mark.skip("Can't run test in github actions")
    def test_batch_get_action(self):
        repo = ActionRepositoryDynamo()
        repo_mock = ActionRepositoryMock()

        action_ids = [action.action_id for action in repo_mock.actions]

        resp = repo.batch_get_action(action_ids)

        expected_actions = repo_mock.actions
        expected_actions.sort(key=lambda x: x.action_id)

        resp.sort(key=lambda x: x.action_id)

        assert resp == repo_mock.actions


    @pytest.mark.skip("Can't run test in github actions")
    def test_update_action(self):
        repo = ActionRepositoryDynamo()
        repo_mock = ActionRepositoryMock()

        action = repo_mock.actions[0]

        resp = repo.update_action(action.action_id, new_description= "Nova descrição", new_user_id="148c6ada-c0d1-7054-66ab-e17414c48ae3", new_is_valid=False)


        assert resp.action_id == action.action_id
        assert resp.description == "Nova descrição"
        assert resp.user_id == "148c6ada-c0d1-7054-66ab-e17414c48ae3"
        assert resp.is_valid == False
        
    @pytest.mark.skip("Can't run test in github actions")
    def test_get_associated_actions_by_user_id(self):
        repo = ActionRepositoryDynamo()
        resp = repo.get_associated_actions_by_user_id(user_id="148c6ada-c0d1-7054-66ab-e17414c48ae3", amount=20, start=1624526000000, end=1676456000000, exclusive_start_key={'action_id' : "5f4f13df-e7d3-4a10-9219-197ceae9e3f0", 'start_date' : 1644256000000})
        
        assert all([type(action) == AssociatedAction for action in resp])
        assert all([action.user_id == "148c6ada-c0d1-7054-66ab-e17414c48ae3" for action in resp])
        assert all([action.start_date >= 1624526000000 for action in resp])
        assert all([action.start_date <= 1676456000000 for action in resp])
        assert all([action.action_id != "5f4f13df-e7d3-4a10-9219-197ceae9e3f0" for action in resp])
        assert len(resp) <= 20

    @pytest.mark.skip("Can't run test in github actions")
    def test_batch_update_associated_action_start(self):
        repo = ActionRepositoryDynamo()

        resp = repo.batch_update_associated_action_start(action_id="7778ee40-d98b-4187-8b02-052b70cc1ec1", new_start_date=1644256000000)
        
        assert all(type(action) == AssociatedAction for action in resp)
        assert all(action.start_date == 1644256000000 for action in resp)
        assert all(action.action_id == "7778ee40-d98b-4187-8b02-052b70cc1ec1" for action in resp)
        
    @pytest.mark.skip("Can't run test in github actions")
    def test_update_project(self):
        repo = ActionRepositoryDynamo()
        resp = repo.update_project(code="MF", new_name="Mauá Fud")

        assert resp.code == "MF"
        assert resp.name == "Mauá Fud"
        
    @pytest.mark.skip("Can't run test in github actions")
    def test_get_project(self):
        repo = ActionRepositoryDynamo()
        repo_mock = ActionRepositoryMock()

        project = repo_mock.projects[0]

        resp = repo.get_project(project.code)

        assert resp == project

    @pytest.mark.skip("Can't run test in github actions")
    def test_batch_update_associated_action_members(self):
        repo = ActionRepositoryDynamo()

        resp = repo.batch_update_associated_action_members(action_id="7778ee40-d98b-4187-8b02-052b70cc1ec1", members=["21010757", "19017311"], user_ids=["148c6ada-c0d1-7054-66ab-e17414c48ae3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3"], start_date=1644256000000)
        
        assert all(type(action) == AssociatedAction for action in resp)
        assert all(action.action_id == "7778ee40-d98b-4187-8b02-052b70cc1ec1" for action in resp)
        assert all(action.member_ra in ["21010757", "19017311"] for action in resp)
        assert all(action.start_date == 1644256000000 for action in resp)
        assert all(action.user_id in ["148c6ada-c0d1-7054-66ab-e17414c48ae3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3"] for action in resp)

    @pytest.mark.skip("Can't run test in github actions")
    def test_batch_get_member(self):
        repo = ActionRepositoryDynamo()
        repo_mock = ActionRepositoryMock()

        members_ra = [member.ra for member in repo_mock.members]

        resp = repo.batch_get_member(members_ra)

        expected_members = repo_mock.members
        expected_members.sort(key=lambda x: x.ra)

        resp.sort(key=lambda x: x.ra)

        assert resp == expected_members

    @pytest.mark.skip("Can't run test in github actions")
    def test_update_action_validation(self):
        repo = ActionRepositoryDynamo()
        repo_mock = ActionRepositoryMock()

        action = repo_mock.actions[0]

        resp = repo.update_action(action.action_id, is_valid=False)


        assert resp.action_id == action.action_id
        assert resp.is_valid == False

    @pytest.mark.skip("Can't run test in github actions")
    def test_update_project_with_member_ids(self):
        repo = ActionRepositoryDynamo()

        resp = repo.update_project("PT", new_members_user_ids=["6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ])

        assert resp.members_user_ids == ['51ah5jaj-c9jm-1345-666ab-e12341c14a3', '6f5g4h7J-876j-0098-123hb-hgb567fy4hb', '93bc6ada-c0d1-7054-66ab-e17414c48ae3']