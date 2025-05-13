from .download_actions_extractor import DownloadActionsExtractor
import pandas as pd
import io

class DownloadActionsTransformer:
    def __init__(self, extractor: DownloadActionsExtractor):
        self.extractor = extractor

    def __call__(self, project_code: str):
        data = self.extractor(project_code)

        df_actions = pd.DataFrame([a.__dict__ for a in data["actions"]])
        df_associated = pd.DataFrame([a.__dict__ for a in data["associated_actions"]])

        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df_actions.to_excel(writer, sheet_name="Ações", index=False)
            df_associated.to_excel(writer, sheet_name="Ações Associadas", index=False)

        output.seek(0)
        return output
