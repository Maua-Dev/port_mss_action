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

        print("entoru no usecase")
    
        if not Member.validate_user_id(user_id):
            raise EntityError('user_id')
        
        member = self.member_repo.get_member(user_id=user_id)

        if member == None:
            raise UnregisteredUser()
        
        is_active = Member.validate_active(member.active)
        
        if start_date is None :
            now = datetime.now()
            year = now.year

            if (now.month <= 6) or (now.month == 12):
                if (now.month <= 6): 
                    start_date = datetime(year-1, 12, 1).timestamp() * 1000
                else:
                    start_date = datetime(year, 12, 1).timestamp() * 1000
            else:  
                start_date = datetime(year, 7, 1).timestamp() * 1000
        

        if end_date is None:
            now = datetime.now()
            year = now.year

            if (now.month <= 6) or (now.month == 12): 
                if (now.month <= 6): 
                    end_date = datetime(year, 6, 30).timestamp() * 1000
                else:
                    end_date = datetime(year+1, 6, 30).timestamp() * 1000
            else:  
                end_date = datetime(year, 11, 30).timestamp() * 1000

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

       

        #verifica se estamos no semestre 1 ou 2
        now= datetime.now()
        year= now.year

        if now.month <= 6:
            start_sem= Decimal(datetime(year, 1, 1).timestamp() * 1000)
            end_sem= Decimal(datetime(year, 6, 30).timestamp() * 1000)

        else:
            start_sem= Decimal(datetime(year, 7, 1).timestamp() * 1000)
            end_sem= Decimal(datetime(year, 12, 31).timestamp() * 1000)

        print("chegou até antes de pegar os strikes")

        #puxa os strikes do usuário
        target_user_list_strike= self.strike_repo.get_strike_by_target_id(target_user_id= member_user_id)

        print("conseguiu puxar os strikes do usuario")
        
        #puxa todos os projetos
        projects= self.action_repo.get_all_projects()
        
        #verifica se o usuário tem strikes neste semestre
        # COMENTEI A LINHA DE BAIXO
        if target_user_list_strike: 
            target_user_list_strike_this_sem= [
                s for s in target_user_list_strike
                if start_sem <= s.occurred_date <= end_sem
            ]

        #se tiver, conta quantos projetos ele está envolvido
        total_projects= 0

        for project in projects:
            if member_user_id in project.members_user_ids:
                total_projects+= 1

        #verifica quantidade de strikes permitidos conforme a quantidade de projetos
        if(total_projects in [0,1]):
            member.strikes_allowed= 2
        if(total_projects == 2):
            member.strikes_allowed= 3
        if(total_projects >= 3):
            member.strikes_allowed= 4
        
        if target_user_list_strike:
            member.strikes= len(target_user_list_strike_this_sem)
        
        else:
            member.strikes= 0

        print("passou da logica dos strikes")
        print(member.strikes_allowed)
        print(member.strikes)

        print(is_active)

        if not is_active:
            raise UserNotAllowed()
        
        print("passou da validacao do isactive")
        
        return member