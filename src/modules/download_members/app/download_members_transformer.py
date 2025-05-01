from .download_members_extractor import DownloadMembersExtractor
import pandas as pd
import io

class DownloadMembersTransformer:
    def __init__(self, extractor: DownloadMembersExtractor):
        self.extractor = extractor

    def __call__(self):
        members = self.extractor()
        df_members = pd.DataFrame.from_dict(members)

        output = io.BytesIO()

        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df_members.to_excel(writer, sheet_name="Membros")

        output.seek(0)

        return output