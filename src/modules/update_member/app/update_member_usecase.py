
from typing import List, Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UpdateMemberUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
        
    def __call__(self, ra: str, new_name: Optional[str] = None, new_email_dev: Optional[str] = None, new_email: Optional[str] = None, new_role: Optional[ROLE] = None, new_stack: Optional[STACK] = None, new_year: Optional[int] = None, new_cellphone: Optional[str] = None, new_course: Optional[COURSE] = None, new_hired_date: Optional[int] = None, new_deactivated_date: Optional[int] = None, new_active: Optional[ACTIVE] = None) -> Member:
        
        if not Member.validate_ra(ra):
            raise EntityError("ra")


        member = self.repo.get_member(ra)
        if not member:
            raise NoItemsFound('member')
        
        
        # members = None
        # start_date = new_start_date if new_start_date is not None else action.start_date
        # if new_associated_members_ra and new_owner_ra:
        #     members = [new_owner_ra] + new_associated_members_ra
        # elif new_associated_members_ra:
        #     members = new_associated_members_ra + [action.owner_ra]
        # elif new_owner_ra:
        #     members = [new_owner_ra] + action.associated_members_ra
        # else:
        #     members = action.associated_members_ra + [action.owner_ra]
        # if members != None and set(members) != set([action.owner_ra] + action.associated_members_ra):
        #     self.repo.batch_update_associated_action_members(action_id, members, start_date=start_date)
        # elif start_date != action.start_date:
        #     self.repo.batch_update_associated_action_members(action_id, members, start_date=new_start_date)
            
        # description = new_description if new_description is not '' else action.description
        # story_id = new_story_id if new_story_id is not -1 else action.story_id        

        return self.repo.update_member(ra, new_name, new_email_dev, new_email, new_role, new_stack, new_year, new_cellphone, new_course, new_hired_date, new_deactivated_date, new_active)