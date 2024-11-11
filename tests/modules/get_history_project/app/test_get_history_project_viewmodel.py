from src.modules.get_history_project.app.get_history_project_usecase import GetHistoryProjectUsecase
from src.modules.get_history_project.app.get_history_project_viewmodel import GetHistoryProjectViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE

class Test_GetHistoryProjectViewmodel:
    def test_get_history_project_viewmodel(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryProjectUsecase(repo, repo_member)
        user = repo_member.get_member(user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3')
        user.active = ACTIVE.ACTIVE
        actions, last_evaluated_key = usecase(
            user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3',project_code='SF')
        viewmodel = GetHistoryProjectViewmodel(
            actions=actions, last_evaluated_key=last_evaluated_key).to_dict()

        expected = {
            "actions": [
                 

                 {
                    "user_id": "6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                    "start_date": 1676476000000,
                    "end_date": 1684306000000,
                    "duration": 7830000000,
                    "action_id": "24c7d7a3-6560-4652-a8d6-f2e4f3f23460",
                    "is_valid": True,
                    "story_id": 368,
                    "title": "Retrospectiva",
                    "description": "Front-End",
                    "project_code": "SF",
                    "associated_members_user_ids": [
                        "7gh5yf5H-857H-1234-75hng-94832hvng1s",
                        "75648hbr-184n-1985-91han-7ghn4HgF182",
                        "51ah5jaj-c9jm-1345-666ab-e12341c14a3"
                    ],
                    "stack_tags": [
                        "INTERNAL"
                    ],
                    "action_type_tag": "DESIGN"
                },
              
                {
                    "user_id": "7gh5yf5H-857H-1234-75hng-94832hvng1s",
                    "start_date": 1658136000000,
                    "end_date": 1678116000000,
                    "duration": 19980000000,
                    "action_id": "ea95d4f7-d5ce-4944-9fa1-ab964655294b",
                    "is_valid": True,
                    "story_id": 435,
                    "title": "Retrospective",
                    "description": "Reunião de planning",
                    "project_code": "SF",
                    "associated_members_user_ids": [
                        "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                        "6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                        "76h35dg4-h76v-1875-987hn-h67gfv45Gt4",
                        "6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                        "75648hbr-184n-1985-91han-7ghn4HgF182"
                    ],
                    "stack_tags": [
                        "FRONTEND"
                    ],
                    "action_type_tag": "DESIGN"
                },

                {
                    "user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                    "start_date": 1656666000000,
                    "end_date": 1687596000000,
                    "duration": 30930000000,
                    "action_id": "7778ee40-d98b-4187-8b02-052b70cc1ec1",
                    "is_valid": True,
                    "story_id": 848,
                    "title": "Daily",
                    "description": "Sprint Planning",
                    "project_code": "SF",
                    "associated_members_user_ids": [
                        "7gh5yf5H-857H-1234-75hng-94832hvng1s",
                        "6574hgyt-785n-9134-18gn4-7gh5uvn36cG"
                    ],
                    "stack_tags": [
                        "INFRA"
                    ],
                    "action_type_tag": "LEARN"
                },

                {
                    "user_id": "6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                    "start_date": 1641896000000,
                    "end_date": 1679686000000,
                    "duration": 37790000000,
                    "action_id": "42e01f11-283c-4925-b0aa-e80ac6c1815a",
                    "is_valid": True,
                    "story_id": 983,
                    "title": "Retrospectiva",
                    "description": "Revisão de sprint",
                    "project_code": "SF",
                    "associated_members_user_ids": [
                        "6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                        "7gh5yf5H-857H-1234-75hng-94832hvng1s",
                        "75648hbr-184n-1985-91han-7ghn4HgF182",
                        "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                        "7465hvnb-143g-1675-86HnG-75hgnFbcg36"
                    ],
                    "stack_tags": [
                        "INFRA"
                    ],
                    "action_type_tag": "WORK"
                }

            ],
            "last_evaluated_key": None,
            "message": "the history was retrieved"
        }

        assert viewmodel == expected