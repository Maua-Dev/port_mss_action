from .download_members_extractor import DownloadMembersExtractor
import pandas as pd
import io

class DownloadMembersTransformer:
    def __init__(self, extractor: DownloadMembersExtractor):
        self.extractor = extractor

    def __call__(self):
        members = self.extractor()
        df_members = pd.DataFrame.from_dict(members, orient = "index")

        output = io.BytesIO()

        df_members.to_csv(output, index = False)

        output.seek(0)

        return output