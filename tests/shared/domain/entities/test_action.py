from src.shared.domain.entities.action import Action
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
import pytest
from src.shared.helpers.errors.domain_errors import EntityError

 
class Test_Action:
    
    def test_action(self):
        action = Action(
            owner_ra="22011020",
            start_time=1577847600000,
            end_time=1577890800000,
            action_id="1234",
            associated_members_ra=["22011021", "22011022"],
            title="Teste",
            description="Apenas um teste",
            project_code="TS",
            stack_tags = [STACK.BACKEND],
            action_type_tags = [ACTION_TYPE.CODE]
        )
        
        assert type(action) == Action
        assert action.owner_ra == "22011020"
        assert action.start_time == 1577847600000
        assert action.end_time == 1577890800000
        assert action.action_id == "1234"
        assert action.associated_members_ra == ["22011021", "22011022"]
        assert action.title == "Teste"
        assert action.description == "Apenas um teste"
        assert action.project_code == "TS"
        assert action.stack_tags == [STACK.BACKEND]
        assert action.action_type_tags == [ACTION_TYPE.CODE]
        assert action.end_time - action.start_time == 12 * 60 * 60 * 1000
        
    def test_action_invalid_len_owner_ra(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="2201102",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_owner_ra_not_string(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra=22011020,
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_owner_ra_not_decimal(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="vitor",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_start_time_not_int(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time="2023-01-24",
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
    
    def test_action_end_time_not_int(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577890800000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time="ontem",
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
        
    def test_action_end_time_less_than_start_time(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577890800000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577847600000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
    
    def test_action_invalid_length_action_id(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="123",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_action_id_not_string(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id=1234,
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
        
    
    def test_action_associated_members_ra_none(self):   
        action = Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=None,
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
        assert action.associated_members_ra == []
            
    def test_action_associated_members_ra_not_list(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra="22011021",
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_invalid_associated_members_ra(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "2201102"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_associated_members_ra_is_not_list_of_str(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=[22011021, 22011022],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_owner_ra_is_in_associated_members_ra(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011020", "22011021"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_associated_members_ra_is_empty_list(self):
        action = Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=[],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
        assert action.associated_members_ra == []
    
    def test_action_title_not_string(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title=1,
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_invalid_title_too_short(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="A",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
    
    def test_action_invalid_title_too_long(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non neque ligula. Sed tempor eu purus quis fringilla. Donec quis maximus neque, sed ullamcorper neque. Quisque varius, nibh sed laoreet egestas, neque turpis egestas nisi, sit amet gravida sem dui sed lacus. Integer non velit sit amet lacus ultrices sagittis vitae nec justo. In hac habitasse platea dictumst. Nullam eu magna id tellus molestie cursus sit amet et massa. Donec varius pulvinar quam id ullamcorper. Nulla sit amet quam purus. Suspendisse a nulla vel ante finibus interdum. Quisque volutpat accumsan orci a sagittis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam eu.",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_description_none(self):
        action = Action(
            owner_ra="22011020",
            start_time=1577847600000,
            action_id="1234",
            associated_members_ra=["22011021", "22011022"],
            title="Teste",
            end_time=1577890800000,
            project_code="TS",
            stack_tags = [STACK.BACKEND],
            action_type_tags = [ACTION_TYPE.CODE]
        ) 
        assert action.description == None
        
    def test_action_description_not_string(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title=123,
                description=1,
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_description_too_short(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                description="A",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_description_too_long(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non neque ligula. Sed tempor eu purus quis fringilla. Donec quis maximus neque, sed ullamcorper neque. Quisque varius, nibh sed laoreet egestas, neque turpis egestas nisi, sit amet gravida sem dui sed lacus. Integer non velit sit amet lacus ultrices sagittis vitae nec justo. In hac habitasse platea dictumst. Nullam eu magna id tellus molestie cursus sit amet et massa. Donec varius pulvinar quam id ullamcorper. Nulla sit amet quam purus. Suspendisse a nulla vel ante finibus interdum. Quisque volutpat accumsan orci a sagittis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam eu.",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
    def test_action_project_code_not_string(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code=1,
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
    
    def test_action_invalid_project_code(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="PORTFOLIO",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE]
            )
            
            
    def test_action_stack_tags_none(self):
        action = Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = None,
                action_type_tags = [ACTION_TYPE.CODE]
        )
        
        assert action.stack_tags == []
    
    def test_action_stack_tags_not_list(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = STACK.BACKEND,
                action_type_tags = [ACTION_TYPE.CODE]
            )
    
    def test_action_stack_tags_tags_not_enum(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND, "FRONTEND"],
                action_type_tags = [ACTION_TYPE.CODE]
            )
    
    def test_action_action_type_tags_none(self):
        action = Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = None
        )
        
        assert action.action_type_tags == []
    
    def test_action_action_type_tags_not_list(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = ACTION_TYPE.CODE
            )
    
    def test_action_action_type_tags_tags_not_enum(self):
        with pytest.raises(EntityError):
            Action(
                owner_ra="22011020",
                start_time=1577847600000,
                action_id="1234",
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_time=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tags = [ACTION_TYPE.CODE, "REVIEW"]
            )
        
    def test_create_action_duplicated_associated_ra(self):
        with pytest.raises(EntityError):
            action = Action(owner_ra='17033730', start_time=1634526000, action_id='82fc', associated_members_ra=['21017310', '21010757', '21010757'], title='Teste', end_time=1577890800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tags=[ACTION_TYPE.CODE])