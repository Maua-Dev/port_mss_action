from src.shared.domain.entities.action import Action
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
import pytest
from src.shared.helpers.errors.domain_errors import EntityError

 
class Test_Action:
    
    def test_action(self):
        action = Action(
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            start_date=1577847600000,
            end_date=1577890800000,
            duration=10 * 60 * 60 * 1000,
            action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
            is_valid=True,
            story_id=100,
            associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
            title="Teste",
            description="Apenas um teste",
            project_code="TS",
            stack_tags = [STACK.BACKEND],
            action_type_tag = ACTION_TYPE.CODE
        )
        
        assert type(action) == Action
        assert action.user_id == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        assert action.start_date == 1577847600000
        assert action.end_date == 1577890800000
        assert action.action_id == "a571c870-d7da-4a25-951c-2ca2d2398a14"
        assert action.is_valid == True
        assert action.story_id == 100
        assert action.associated_members_user_ids == ["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"]
        assert action.title == "Teste"
        assert action.description == "Apenas um teste"
        assert action.project_code == "TS"
        assert action.stack_tags == [STACK.BACKEND]
        assert action.action_type_tag == ACTION_TYPE.CODE
        assert action.end_date - action.start_date == 12 * 60 * 60 * 1000
        
            
    def test_action_start_date_not_int(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date="2023-01-24",
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
    
    def test_action_end_date_not_int(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577890800000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date="ontem",
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
        
    def test_action_end_date_less_than_start_date(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577890800000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577847600000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
    
    def test_action_invalid_length_action_id(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="1234",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
            
    def test_action_action_id_not_string(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id=1234,
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
    def test_action_story_id_is_none(self):
        action = Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=None,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
        assert action.story_id == None
        
    def test_action_action_id_not_uuid(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="fgh6s4xx266vnbgih97icvr0qhtsc7x99dgf",
                is_valid=True,
                story_id=None,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )

    def test_action_story_id_not_int(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id="100",
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )

    def test_action_story_id_less_than_minimum(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=0,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )

    def test_action_story_id_greater_than_max(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=1000000000,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )            

    def test_action_associated_members_user_ids_none(self):   
        action = Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=[],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
        assert action.associated_members_user_ids == []
            
    def test_action_associated_members_user_ids_not_list(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
            
    def test_action_invalid_associated_members_user_ids(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj--1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
            
    # def test_action_associated_members_user_ids_is_not_list_of_str(self):
    #     with pytest.raises(EntityError):
    #         Action(
    #             user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
    #             start_date=1577847600000,
    #             action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
    #             is_valid=True,
    #             story_id=100,
    #             duration=10 * 60 * 60 * 1000,
    #             associated_members_user_ids=[22011021, 22011022],
    #             title="Teste",
    #             end_date=1577890800000,
    #             project_code="TS",
    #             stack_tags = [STACK.BACKEND],
    #             action_type_tag = ACTION_TYPE.CODE
    #         )
            
    def test_action_user_id_is_in_associated_members_user_ids(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["93bc6ada-c0d1-7054-66ab-e17414c48ae3", "nsdijfn1-c0d1-7054-66ab-e17414c48ae3"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
            
    def test_action_associated_members_user_ids_is_empty_list(self):
        action = Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=[],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
        assert action.associated_members_user_ids == []
    
    def test_action_title_not_string(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title=1,
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
            
    def test_action_invalid_title_too_short(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="A",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
    
    def test_action_invalid_title_too_long(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non neque ligula. Sed tempor eu purus quis fringilla. Donec quis maximus neque, sed ullamcorper neque. Quisque varius, nibh sed laoreet egestas, neque turpis egestas nisi, sit amet gravida sem dui sed lacus. Integer non velit sit amet lacus ultrices sagittis vitae nec justo. In hac habitasse platea dictumst. Nullam eu magna id tellus molestie cursus sit amet et massa. Donec varius pulvinar quam id ullamcorper. Nulla sit amet quam purus. Suspendisse a nulla vel ante finibus interdum. Quisque volutpat accumsan orci a sagittis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam eu.",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
            
    def test_action_description_none(self):
        action = Action(
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            start_date=1577847600000,
            action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
            is_valid=True,
            story_id=100,
            duration=10 * 60 * 60 * 1000,
            associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
            title="Teste",
            end_date=1577890800000,
            project_code="TS",
            stack_tags = [STACK.BACKEND],
            action_type_tag = ACTION_TYPE.CODE
        ) 
        assert action.description == None
        
    def test_action_description_not_string(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title=123,
                description=1,
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
            
    def test_action_description_too_short(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                description="A",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
            
    def test_action_description_too_long(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non neque ligula. Sed tempor eu purus quis fringilla. Donec quis maximus neque, sed ullamcorper neque. Quisque varius, nibh sed laoreet egestas, neque turpis egestas nisi, sit amet gravida sem dui sed lacus. Integer non velit sit amet lacus ultrices sagittis vitae nec justo. In hac habitasse platea dictumst. Nullam eu magna id tellus molestie cursus sit amet et massa. Donec varius pulvinar quam id ullamcorper. Nulla sit amet quam purus. Suspendisse a nulla vel ante finibus interdum. Quisque volutpat accumsan orci a sagittis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam eu.",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
            
    def test_action_project_code_not_string(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code=1,
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
    
    def test_action_invalid_project_code(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="PORTFOLIO",
                stack_tags = [STACK.BACKEND],
                action_type_tag = ACTION_TYPE.CODE
            )
            
            
    def test_action_stack_tags_none(self):
       with pytest.raises(EntityError):
        Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = None,
                action_type_tag = ACTION_TYPE.CODE
        )
    
    def test_action_stack_tags_not_list(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = STACK.BACKEND,
                action_type_tag = ACTION_TYPE.CODE
            )
    
    def test_action_stack_tags_tags_not_enum(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND, "FRONTEND"],
                action_type_tag = ACTION_TYPE.CODE
            )
    
    def test_action_action_type_tag_none(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = None
        )
        
    def test_action_action_type_tag_tag_not_enum(self):
        with pytest.raises(EntityError):
            Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id=100,
                duration=10 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag = "ACTION_TYPE.CODE"
            )
        
    def test_action_duplicated_associated_ra(self):
        with pytest.raises(EntityError):
            action = Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000, 
                action_id='82fc', 
                story_id=100,
                is_valid=True, 
                duration = 10 * 60 * 60 * 1000, 
                associated_members_user_ids=['21017310', '21010757', '21010757'], 
                title='Teste', 
                end_date=1577890800000, 
                project_code='MF', 
                stack_tags=[STACK.BACKEND], 
                action_type_tag=ACTION_TYPE.CODE
            )

            
    def test_action_duration_none(self):
        with pytest.raises(EntityError):
            action = Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", 
                start_date=1577847600000, 
                action_id='82fc', 
                story_id=100,
                is_valid=True, 
                duration = None, 
                associated_members_user_ids=['21017310', '21010757'], 
                title='Teste', 
                end_date=1577890800000, 
                project_code='MF', 
                stack_tags=[STACK.BACKEND], 
                action_type_tag=ACTION_TYPE.CODE
            )
            
    def test_action_duration_not_int(self):
        with pytest.raises(EntityError):
            action = Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", 
                start_date=1577847600000, 
                action_id='82fc', 
                story_id=100,
                is_valid=True, 
                duration = '10', 
                associated_members_user_ids=['21017310', '21010757'], 
                title='Teste', 
                end_date=1577890800000, 
                project_code='MF', 
                stack_tags=[STACK.BACKEND], 
                action_type_tag=ACTION_TYPE.CODE
            )
            
    def test_action_duration_negative(self):
        with pytest.raises(EntityError):
            action = Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", 
                start_date=1577847600000, 
                action_id='82fc', 
                story_id=100,
                is_valid=True, duration = -1, 
                associated_members_user_ids=['21017310', '21010757'], 
                title='Teste', 
                end_date=1577890800000, 
                project_code='MF', 
                stack_tags=[STACK.BACKEND], 
                action_type_tag=ACTION_TYPE.CODE
            )
            
    def test_action_duration_zero(self):
        with pytest.raises(EntityError):
            action = Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", 
                start_date=1577847600000, 
                action_id='82fc', 
                story_id=100,
                is_valid=True, 
                duration = 0, 
                associated_members_user_ids=['21017310', '21010757'], 
                title='Teste', 
                end_date=1577890800000, 
                project_code='MF', 
                stack_tags=[STACK.BACKEND], 
                action_type_tag=ACTION_TYPE.CODE
            )
            
    def test_action_invalid_duration(self): #duration > end_date - start_date
        with pytest.raises(EntityError):
            action = Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", 
                start_date=1577847600000, 
                action_id='82fc', 
                story_id=100,
                is_valid=True, 
                duration = 48000000, 
                associated_members_user_ids=['21017310', '21010757'], 
                title='Teste', 
                end_date=1577890800000, 
                project_code='MF', 
                stack_tags=[STACK.BACKEND], 
                action_type_tag=ACTION_TYPE.CODE
            ) 

    def test_action_is_valid_not_boolean(self):
        with pytest.raises(EntityError):
            action = Action(
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", 
                start_date=1577847600000, 
                action_id='82fc', 
                story_id=100, 
                duration = 36000000, 
                associated_members_user_ids=['21017310', '21010757'], 
                title='Teste', 
                end_date=1577890800000, 
                project_code='MF', 
                stack_tags=[STACK.BACKEND], 
                action_type_tag=ACTION_TYPE.CODE,
                is_valid=1
            )


    def test_action_user_id_not_string(self):
        with pytest.raises(EntityError):
            action = Action(
                user_id=93, 
                start_date=1577847600000, 
                action_id='82fc', 
                story_id=100, 
                duration = 36000000, 
                associated_members_user_ids=['21017310', '21010757'], 
                title='Teste', 
                end_date=1577890800000, 
                project_code='MF', 
                stack_tags=[STACK.BACKEND], 
                action_type_tag=ACTION_TYPE.CODE,
                is_valid=True
            )

    def test_action_user_id_wrong_length(self):
        with pytest.raises(EntityError):
            action = Action(
                user_id='1', 
                start_date=1577847600000, 
                action_id='82fc', 
                story_id=100, 
                duration = 36000000, 
                associated_members_user_ids=['21017310', '21010757'], 
                title='Teste', 
                end_date=1577890800000, 
                project_code='MF', 
                stack_tags=[STACK.BACKEND], 
                action_type_tag=ACTION_TYPE.CODE,
                is_valid=True
            )