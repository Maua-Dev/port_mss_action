from src.shared.domain.entities.member import Member
from typing import List

class GetMemberInfoViewModel:
    def __init__(self, members: List[Member]):
        self.members = members

    def to_dict(self):
        response = {
            "ALL": []
        }

        for member in self.members:
            member_dict = {
                'name': member.name,
                'ra': member.ra,
                'role': member.role.value,
                'stack': member.stack.value,
                'year': member.year,
                'course': member.course.value,
                'project': member.project if hasattr(member, 'project') else [],
                'hired_date': member.hired_date,
                'photo': member.photo
            }

            response["ALL"].append(member_dict)

            stack_name = member.stack.value

            if stack_name not in response:
                response[stack_name] = []

            response[stack_name].append(member_dict)

        return response