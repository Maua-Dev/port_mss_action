import pytest
import datetime
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.helpers.errors.domain_errors import EntityError


class Test_AssociatedAction:
    
    def test_associated_action(self):
        action = Action(
            owner_ra="22011020",
            start_date=1577847600000,
            duration=3 * 60 * 60 * 1000, 
            action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
            story_id= 100,
            associated_members_ra=["22011021", "22011022"],
            title="Teste",
            end_date=1577890800000,
            project_code="TS",
            stack_tags = [STACK.BACKEND],
            action_type_tag= ACTION_TYPE.CODE
        )

        associated_action = AssociatedAction(member_ra="22011020", action=action)        
        
        assert associated_action.member_ra == "22011020"
        assert associated_action.action == action
        
    def test_associated_action_member_ra_not_string(self):
        action = Action(
                owner_ra="22011020",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                story_id= 100,
                duration=3 * 60 * 60 * 1000,
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag= ACTION_TYPE.CODE
        )
        with pytest.raises(EntityError):
            AssociatedAction(member_ra=22011020, action=action)
    
    def test_associated_action_member_ra_not_decimal(self):
        action = Action(
                owner_ra="22011020",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                story_id= 100,
                duration=3 * 60 * 60 * 1000,
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag= ACTION_TYPE.CODE
        )
        with pytest.raises(EntityError):
            AssociatedAction(member_ra="vitor", action=action)
            
    def test_associated_action_member_ra_invalid_length(self):
        action = Action(
                owner_ra="22011020",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                story_id= 100,
                duration=3 * 60 * 60 * 1000,
                associated_members_ra=["22011021", "22011022"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag= ACTION_TYPE.CODE
        )
        with pytest.raises(EntityError):
            AssociatedAction(member_ra="2201102", action=action)

    def test_associated_action_action_must_be_Action(self):
        action = 1
        
        with pytest.raises(EntityError):
            AssociatedAction(member_ra="2201102", action=action)
    
        