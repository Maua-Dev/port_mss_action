import os
import tempfile
import pytest

from src.modules.download_members.app.download_members_extractor import DownloadMembersExtractor
from src.modules.download_members.app.download_members_transformer import DownloadMembersTransformer
from src.shared.infra.repositories.member_repository_dynamo import MemberRepositoryDynamo

class TestDownloadMembersTransformer:

    def test_download_members_transformer(self):
        
        repo = MemberRepositoryDynamo()
        extractor = DownloadMembersExtractor(repo)

        transformer = DownloadMembersTransformer(extractor=extractor)

        output = transformer()

        with tempfile.NamedTemporaryFile(delete=False, suffix = ".xlsx") as temp_file:
            temp_file.write(output.read())
            temp_file_path = temp_file.name

        os.startfile(temp_file_path)