from datetime import datetime
from decimal import Decimal
from typing import Optional, Tuple
import uuid
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository

from src.shared.domain.repositories.strike_repository_interface import IStrikeRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, UnregisteredUser, UserIsNotFromAdmin, UserIsNotFromRH


class CreateStrikeUsecase:
    def __init__(self, repo: IStrikeRepository, repo_member: IMemberRepository, repo_action: IActionRepository):
        self.repo= repo
        self.repo_member= repo_member
        self.repo_action= repo_action

    def __call__(self, owner_user_id: str, target_user_id: str,applier_user_id: str, occurred_date: int, category: STRIKE_CATEGORY,description: Optional [str] = None) -> Tuple[Strike, int]:

        strike_id= str(uuid.uuid4())

        strike=Strike(
            strike_id= strike_id,
            owner_user_id= owner_user_id,
            target_user_id= target_user_id,
            applier_user_id= applier_user_id,
            occurred_date= occurred_date,
            category= category,
            description= description
        )

        if not self.repo_member.get_member(user_id=owner_user_id) or not self.repo_member.get_member(user_id=applier_user_id) or not self.repo_member.get_member(user_id=target_user_id):
            raise UnregisteredUser()
        
        owner_user= self.repo_member.get_member(user_id=owner_user_id)

        if not Member.validate_role_admin(role= owner_user.role):
            raise ForbiddenAction('Owner user is not a director')
        
        applier_user= self.repo_member.get_member(user_id=applier_user_id)

        if not Member.validate_active(active=applier_user.active):
            raise ForbiddenAction("RH member is not active")
        
        if applier_user.role is ROLE.INTERNAL:
            if applier_user.stack is not STACK.RH:
                raise UserIsNotFromRH(user='applier user')
            
        elif not Member.validate_role_admin(role=applier_user.role):
            raise ForbiddenAction('Applier user is not a director')
        
        target_user= self.repo_member.get_member(user_id=target_user_id)

        if not Member.validate_active(active=target_user.active):
            raise ForbiddenAction('target user is not active')
        
        now= datetime.now()
        year= now.year

        if now.month <= 6:
            start_sem= Decimal(datetime(year, 1, 1).timestamp() * 1000)
            end_sem= Decimal(datetime(year, 6, 30).timestamp() * 1000)

        else:
            start_sem= Decimal(datetime(year, 7, 1).timestamp() * 1000)
            end_sem= Decimal(datetime(year, 12, 31).timestamp() * 1000)

        created_strike= self.repo.create_strike(strike=strike)

        taget_user_list_stike= self.repo.get_strike_by_target_id(target_user_id=target_user_id) or []

        projects= self.repo_action.get_all_projects()

        
        target_user_list_strike_this_sem= [
            s for s in taget_user_list_stike
            if start_sem <= s.occurred_date <= end_sem 
        ]

        total_projects= 0

        for project in projects:
            # aqui ficar de olho porque na minha cabeca faz sentido fazer o in e nao o ==
            if target_user_id in project.members_user_ids:
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
        
    # fazer uma logica parecida com o que esta no auth user, mandando uma mensagem caso as horas sejam zeradas e uma caso seja so criado o strike