from .download_actions_extractor import DownloadActionsExtractor
import pandas as pd
import io

class DownloadActionsTransformer:
    def __init__(self, extractor: DownloadActionsExtractor):
        self.extractor = extractor

    def __call__(self):
        actions = self.extractor()
        df_actions = pd.DataFrame.from_dict(actions)

        output = io.BytesIO()

        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df_actions.to_excel(writer, sheet_name="Ações")

        output.seek(0)

        return output