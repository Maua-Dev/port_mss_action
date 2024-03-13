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
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            start_date=1577847600000,
            duration=3 * 60 * 60 * 1000, 
            action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
            is_valid=True,
            story_id= 100,
            associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
            title="Teste",
            end_date=1577890800000,
            project_code="TS",
            stack_tags = [STACK.BACKEND],
            action_type_tag= ACTION_TYPE.CODE
        )

        associated_action = AssociatedAction(
            member_ra="22011020", 
            action_id=action.action_id, 
            start_date=action.start_date,
            user_id=action.user_id
            )        
        
        assert associated_action.member_ra == "22011020"
        assert associated_action.action_id == action.action_id
        assert associated_action.start_date == action.start_date
        assert associated_action.user_id == action.user_id
        
    def test_associated_action_member_ra_not_string(self):
        action = Action(
                owner_ra="22011020",
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id= 100,
                duration=3 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag= ACTION_TYPE.CODE
        )
        with pytest.raises(EntityError):
            AssociatedAction(member_ra=22011020, 
                             action_id=action.action_id, 
                             start_date=action.start_date,
                             user_id=action.user_id)
    
    def test_associated_action_member_ra_not_decimal(self):
        action = Action(
                owner_ra="22011020",
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id= 100,
                duration=3 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag= ACTION_TYPE.CODE
        )
        with pytest.raises(EntityError):
            AssociatedAction(member_ra="vitor", 
                             action_id=action.action_id, 
                             start_date=action.start_date,
                             user_id=action.user_id)
            
    def test_associated_action_member_ra_invalid_length(self):
        action = Action(
                owner_ra="22011020",
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id= 100,
                duration=3 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag= ACTION_TYPE.CODE
        )
        with pytest.raises(EntityError):
            AssociatedAction(member_ra="2201102", 
                             action_id=action.action_id, 
                             start_date=action.start_date, 
                             user_id=action.user_id)

    def test_associated_action_action_id_must_be_uuid(self):
        with pytest.raises(EntityError):
            AssociatedAction(member_ra="2201102", 
                             action_id=1, 
                             start_date=1577847600000,
                             user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3")
            
    def test_associated_action_start_date_not_int(self):
        action = Action(
                owner_ra="22011020",
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1577847600000,
                action_id="a571c870-d7da-4a25-951c-2ca2d2398a14",
                is_valid=True,
                story_id= 100,
                duration=3 * 60 * 60 * 1000,
                associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb"],
                title="Teste",
                end_date=1577890800000,
                project_code="TS",
                stack_tags = [STACK.BACKEND],
                action_type_tag= ACTION_TYPE.CODE
        )
        with pytest.raises(EntityError):
            AssociatedAction(member_ra="22011020", 
                             action_id=action.action_id, 
                             start_date="1577847600000",
                             user_id=action.user_id)
            
    def test_associated_action_user_id_not_string(self):
        with pytest.raises(EntityError):
            AssociatedAction(member_ra="22011020", 
                             action_id="a571c870-d7da-4a25-951c-2ca2d2398a14", 
                             start_date=1577847600000,
                             user_id=1)
            
    def test_associated_action_user_id_invalid_length(self):
        with pytest.raises(EntityError):
            AssociatedAction(member_ra="22011020", 
                             action_id="a571c870-d7da-4a25-951c-2ca2d2398a14", 
                             start_date=1577847600000,
                             user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae")