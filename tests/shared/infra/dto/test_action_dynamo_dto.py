from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.dto.action_dynamo_dto import ActionDynamoDTO


class Test_ActionDynamoDTO:

    def test_action_dynamo_dto_from_entity(self):
        action = Action(owner_ra="10017310",
                        action_id="5f4f13df-e7d3-4a10-9219-197ceae9e3f0",
                        is_valid=True,
                        story_id=94,
                        associated_members_ra=["23017310","21010757","22017310","21017310","19017310", "19017311"],
                        stack_tags=[STACK.INFRA],
                        action_type_tag=ACTION_TYPE.CODEREVIEW,
                        project_code="PT",
                        title="Retrospectiva",
                        description="Revisão de sprint",
                        start_date=1644256000000,
                        end_date=1653756000000,
                        duration=9500000000)

        action_dto = ActionDynamoDTO.from_entity(action)
        assert action_dto == ActionDynamoDTO(owner_ra="10017310", action_id="5f4f13df-e7d3-4a10-9219-197ceae9e3f0", is_valid=True, story_id=94, associated_members_ra=[
                                             "23017310", "21010757", "22017310", "21017310", "19017310", "19017311"], stack_tags=[STACK.INFRA], action_type_tag=ACTION_TYPE.CODEREVIEW, project_code="PT", title="Retrospectiva", description="Revisão de sprint", start_date=1644256000000, end_date=1653756000000, duration=9500000000)
        
    def test_action_dynamo_dto_to_dynamo(self):
        action_dto = ActionDynamoDTO(owner_ra="10017310", action_id="5f4f13df-e7d3-4a10-9219-197ceae9e3f0", is_valid=True, story_id=94, associated_members_ra=[
                                             "23017310", "21010757", "22017310", "21017310", "19017310", "19017311"], stack_tags=[STACK.INFRA], action_type_tag=ACTION_TYPE.CODEREVIEW, project_code="PT", title="Retrospectiva", description="Revisão de sprint", start_date=1644256000000, end_date=1653756000000, duration=9500000000)
        
        action_dynamo = action_dto.to_dynamo()
        
        assert action_dynamo == {
            'entity': 'action',
            'owner_ra': '10017310',
            'start_date': 1644256000000,
            'stack_tags': ['INFRA'],
            'end_date': 1653756000000,
            'duration': 9500000000,
            'action_id': '5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
            'is_valid': eval('True'),
            'story_id': 94,
            'title': 'Retrospectiva',
            'description': 'Revisão de sprint',
            'project_code': 'PT',
            'associated_members_ra': ['23017310', '21010757', '22017310', '21017310', '19017310', '19017311'],
            'action_type_tag': 'CODEREVIEW'
        }
        
    def test_action_dynamo_dto_from_dynamo(self): 
        action_dynamo = {
            'entity': 'action',
            'owner_ra': '10017310',
            'start_date': 1644256000000,
            'stack_tags': ['INFRA'],
            'end_date': 1653756000000,
            'duration': 9500000000,
            'action_id': '5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
            'is_valid': eval('True'),
            'story_id': 94,
            'title': 'Retrospectiva',
            'description': 'Revisão de sprint',
            'project_code': 'PT',
            'associated_members_ra': ['23017310', '21010757', '22017310', '21017310', '19017310', '19017311'],
            'action_type_tag': 'CODEREVIEW'
        }
        
        action_dto = ActionDynamoDTO.from_dynamo(action_dynamo)
        
        assert action_dto == ActionDynamoDTO(owner_ra="10017310", action_id="5f4f13df-e7d3-4a10-9219-197ceae9e3f0", is_valid=True, story_id=94, associated_members_ra=[
                                             "23017310", "21010757", "22017310", "21017310", "19017310", "19017311"], stack_tags=[STACK.INFRA], action_type_tag=ACTION_TYPE.CODEREVIEW, project_code="PT", title="Retrospectiva", description="Revisão de sprint", start_date=1644256000000, end_date=1653756000000, duration=9500000000)
        
    def test_action_dynamo_dto_to_entity(self):
        action_dto = ActionDynamoDTO(owner_ra="10017310", action_id="5f4f13df-e7d3-4a10-9219-197ceae9e3f0", is_valid=True, story_id=94, associated_members_ra=[
                                             "23017310", "21010757", "22017310", "21017310", "19017310", "19017311"], stack_tags=[STACK.INFRA], action_type_tag=ACTION_TYPE.CODEREVIEW, project_code="PT", title="Retrospectiva", description="Revisão de sprint", start_date=1644256000000, end_date=1653756000000, duration=9500000000)
        
        action = action_dto.to_entity()
        
        assert action == Action(owner_ra="10017310",
                        action_id="5f4f13df-e7d3-4a10-9219-197ceae9e3f0",
                        is_valid=True,
                        story_id=94,
                        associated_members_ra=["23017310","21010757","22017310","21017310","19017310", "19017311"],
                        stack_tags=[STACK.INFRA],
                        action_type_tag=ACTION_TYPE.CODEREVIEW,
                        project_code="PT",
                        title="Retrospectiva",
                        description="Revisão de sprint",
                        start_date=1644256000000,
                        end_date=1653756000000,
                        duration=9500000000)
        
    def test_action_dynamo_dto_from_entity_to_dynamo(self):
        action = Action(owner_ra="10017310",
                        action_id="5f4f13df-e7d3-4a10-9219-197ceae9e3f0",
                        is_valid=True,
                        story_id=94,
                        associated_members_ra=["23017310","21010757","22017310","21017310","19017310", "19017311"],
                        stack_tags=[STACK.INFRA],
                        action_type_tag=ACTION_TYPE.CODEREVIEW,
                        project_code="PT",
                        title="Retrospectiva",
                        description="Revisão de sprint",
                        start_date=1644256000000,
                        end_date=1653756000000,
                        duration=9500000000)

        action_dynamo = ActionDynamoDTO.from_entity(action).to_dynamo()
        
        assert action_dynamo == {
            'entity': 'action',
            'owner_ra': '10017310',
            'start_date': 1644256000000,
            'stack_tags': ['INFRA'],
            'end_date': 1653756000000,
            'duration': 9500000000,
            'action_id': '5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
            'is_valid': eval('True'),
            'story_id': 94,
            'title': 'Retrospectiva',
            'description': 'Revisão de sprint',
            'project_code': 'PT',
            'associated_members_ra': ['23017310', '21010757', '22017310', '21017310', '19017310', '19017311'],
            'action_type_tag': 'CODEREVIEW'
        }
        
    def test_action_dynamo_dto_from_dynamo_to_entity(self): 
        action_dynamo = {
            'entity': 'action',
            'owner_ra': '10017310',
            'start_date': 1644256000000,
            'stack_tags': ['INFRA'],
            'end_date': 1653756000000,
            'duration': 9500000000,
            'action_id': '5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
            'is_valid': eval('True'),
            'story_id': 94,
            'title': 'Retrospectiva',
            'description': 'Revisão de sprint',
            'project_code': 'PT',
            'associated_members_ra': ['23017310', '21010757', '22017310', '21017310', '19017310', '19017311'],
            'action_type_tag': 'CODEREVIEW'
        }
        
        action = ActionDynamoDTO.from_dynamo(action_dynamo).to_entity()
        
        assert action == Action(owner_ra="10017310",
                        action_id="5f4f13df-e7d3-4a10-9219-197ceae9e3f0",
                        is_valid=True,
                        story_id=94,
                        associated_members_ra=["23017310","21010757","22017310","21017310","19017310", "19017311"],
                        stack_tags=[STACK.INFRA],
                        action_type_tag=ACTION_TYPE.CODEREVIEW,
                        project_code="PT",
                        title="Retrospectiva",
                        description="Revisão de sprint",
                        start_date=1644256000000,
                        end_date=1653756000000,
                        duration=9500000000)