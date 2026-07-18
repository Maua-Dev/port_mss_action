from src.shared.domain.entities.member import Member
from typing import List

class PortfolioExportMembersViewModel:
    def __init__(self, members: List[Member]):
        self.members = members

    def to_dict(self):
        home_carousel = []
        quote_carousel = []
        member_carousel = []

        for member in self.members:
            home_carousel.append({
                "name": member.name,
                "photoPath": member.photo,
                "area": member.stack.value if hasattr(member, 'stack') and member.stack else ""
            })

            quote_carousel.append({
                "name": member.name,
                "quote": getattr(member, 'quote', ""),
                "photoPath": member.photo,
                "role": member.role.value if hasattr(member, 'role') and member.role else ""
            })

            member_carousel.append({
                "name": member.name,
                "photoPath": member.photo,
                "email": getattr(member, 'email', ""),
                "role": member.role.value if hasattr(member, 'role') and member.role else "",
                "phone": getattr(member, 'phone', "")
            })

        return {
            "homeCarousel": home_carousel,
            "quoteCarousel": quote_carousel,
            "memberCarousel": member_carousel
        }
