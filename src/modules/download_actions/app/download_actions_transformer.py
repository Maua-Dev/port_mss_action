from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from .download_actions_extractor import DownloadActionsExtractor
import pandas as pd
import io

class DownloadActionsTransformer:
    def __init__(self, extractor: DownloadActionsExtractor, repo: IMemberRepository):
        self.extractor = extractor
        self.member_repo = repo

    def __call__(self, project_code: str):
        data = self.extractor(project_code)
        all_actions = data["actions"] + data["associated_actions"]

        df_actions = pd.DataFrame([a.__dict__ for a in all_actions])

        if not all_actions:
            raise NoItemsFound("actions")
        
        if "associated_members_user_ids" in df_actions.columns:
            df_actions = df_actions.drop(columns=["associated_members_user_ids"])
        
        if "project_code" in df_actions.columns:
            df_actions = df_actions.drop(columns=["project_code"])
            
        user_ids = set(df_actions['user_id'].dropna().unique())

        user_map = {}

        for user_id in user_ids:
            member = self.member_repo.get_member(user_id)
            if member:
                user_map[user_id] = member.name
            else:
                user_map[user_id] = ""
        
        df_actions['member_name'] = df_actions['user_id'].map(user_map)

        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df_actions.to_excel(writer, sheet_name="Ações", index=False)

        output.seek(0)
        return output
