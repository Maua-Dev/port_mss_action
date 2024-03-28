from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.infra.dto.associated_action_dynamo_dto import AssociatedActionDynamoDTO

class Test_AssociatedActionDynamoDTO:
    def test_associated_action_dynamo_dto_from_entity(self):
        associated_action = AssociatedAction(action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',start_date=1644256000000, user_id='6f5g4h7J-876j-0098-123hb-hgb567fy4hb')
        associated_action_dto = AssociatedActionDynamoDTO.from_entity(associated_action)
        
        assert associated_action_dto == AssociatedActionDynamoDTO(action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0', start_date=1644256000000, user_id='6f5g4h7J-876j-0098-123hb-hgb567fy4hb')
        
    def test_associated_action_dynamo_dto_to_dynamo(self):
        associated_action_dto = AssociatedActionDynamoDTO(action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',start_date=1644256000000, user_id='6f5g4h7J-876j-0098-123hb-hgb567fy4hb')
        associated_action_dynamo = associated_action_dto.to_dynamo()
        
        assert associated_action_dynamo == {'entity': 'associated_action', 'action_id': '5f4f13df-e7d3-4a10-9219-197ceae9e3f0', 'start_date': 1644256000000, 'user_id': '6f5g4h7J-876j-0098-123hb-hgb567fy4hb'}
        
    def test_associated_action_dynamo_dto_from_dynamo(self):
        associated_action_dynamo = {'entity': 'associated_action', 'action_id': '5f4f13df-e7d3-4a10-9219-197ceae9e3f0', 'start_date': 1644256000000, 'user_id': '6f5g4h7J-876j-0098-123hb-hgb567fy4hb'}
        associated_action_dto = AssociatedActionDynamoDTO.from_dynamo(associated_action_dynamo)
        
        assert associated_action_dto == AssociatedActionDynamoDTO(action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',start_date=1644256000000, user_id='6f5g4h7J-876j-0098-123hb-hgb567fy4hb')
        
    def test_associated_action_dynamo_dto_to_entity(self):
        associated_action_dto = AssociatedActionDynamoDTO(action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',start_date=1644256000000, user_id='6f5g4h7J-876j-0098-123hb-hgb567fy4hb')
        associated_action = associated_action_dto.to_entity()
        
        assert associated_action == AssociatedAction(action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',start_date=1644256000000, user_id='6f5g4h7J-876j-0098-123hb-hgb567fy4hb')