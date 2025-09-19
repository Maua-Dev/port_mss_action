from datetime import datetime
from decimal import Decimal
from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.strike_repository_interface import IStrikeRepository

from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed


class GetMemberUsecase:
    def __init__(self, member_repo: IMemberRepository, action_repo: IActionRepository, strike_repo: IStrikeRepository):
        self.strike_repo = strike_repo
        self.member_repo = member_repo
        self.action_repo = action_repo
        
    def __call__(self,user_id: str, start_date: Optional[int] = None, end_date: Optional[int] = None) -> Member:
    
        if not Member.validate_user_id(user_id):
            raise EntityError('user_id')
        
        member = self.member_repo.get_member(user_id=user_id)

        if member == None:
            raise UnregisteredUser()
        
        is_active = Member.validate_active(member.active)
        
        if start_date is None :
            now = datetime.now()
            year = now.year

            if now.month <= 6: 
                start_date = datetime(year, 1, 1).timestamp() * 1000
            else:  
                start_date = datetime(year, 7, 1).timestamp() * 1000
        

        if end_date is None:
            now = datetime.now()
            year = now.year

            if now.month <= 6: 
                end_date = datetime(year, 6, 30).timestamp() * 1000
            else:  
                end_date = datetime(year, 12, 31).timestamp() * 1000

        start_date, end_date = Decimal(start_date), Decimal(end_date)

        hours_worked = self.action_repo.get_all_actions_durations_by_user_id(start_date, end_date)
        
        member_user_id = member.user_id
        
        member.hours_worked = hours_worked.get(member_user_id, [])

        projects = self.action_repo.get_all_projects()

        member_projects = {member.user_id: []}
        
        for project in projects:
            project_name = project.name
            for member_user_id in project.members_user_ids:
                if member_user_id in member_projects:
                    member_projects[member_user_id].append(project_name)

        member_user_id = member.user_id
        member.hours_worked = hours_worked.get(member_user_id, 0)
        member.project = member_projects.get(member_user_id, [])

        # Código novo a partir daqui
        target_user_list_strike= self.repo.get_strike_by_target_id(target_user_id= member_user_id)

        projects= self.repo_action.get_all_projects()

        if target_user_list_strike:
            target_user_list_strike_this_sem= [
                s for s in target_user_list_strike
                if start_sem <= s.occurred_date <= end_sem
            ]

            total_projects= 0

            for project in projects:
                if project.members_user_ids == target_user_id:
                    total_projects+= 1

            if (total_projects in [0, 1] and len(target_user_list_strike_this_sem) > 2) or (total_projects == 2 and len(target_user_list_strike_this_sem) > 3) or (total_projects >= 3 and len(target_user_list_strike_this_sem) > 4):

                target_user_hours_workerd= self.repo_action.get_action_durations_for_user(user_id=target_user_id, start_date=start_sem, end_date=end_sem)

                action_id= str(uuid.uuid4())

                strike_action=Action(
                    user_id=target_user_id,
                    start_date=(int(start_sem) + target_user_hours_workerd),
                    stack_tags=[target_user.stack],
                    end_date=int(start_sem),
                    duration=-target_user_hours_workerd,
                    action_id=action_id,
                    is_valid=True,
                    title="ZERAGEM DE HORAS",
                    project_code="HZ",
                    action_type_tag= ACTION_TYPE.HOURS_RESET,
                    description="Ação criada devido ao atingimento do limite de strikes"
                )

                self.repo_action.create_action(action=strike_action)

                return (created_strike, 1)

            return (created_strike, 0)
       
        if not is_active:
            raise UserNotAllowed()
        
        return member