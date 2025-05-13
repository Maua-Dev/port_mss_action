import os
import tempfile
import pytest

from src.modules.download_actions.app.download_actions_extractor import DownloadActionsExtractor
from src.modules.download_actions.app.download_actions_transformer import DownloadActionsTransformer
from src.shared.infra.repositories.action_repository_dynamo import ActionRepositoryDynamo

class TestDownloadActionsTransformer:

   #@pytest.mark.skip("Can't run test in gh actions")
    def test_download_actions_transformer(self):
        
        repo = ActionRepositoryDynamo()
        extractor = DownloadActionsExtractor(repo)

        transformer = DownloadActionsTransformer(extractor=extractor)

        output = transformer("SM")

        with tempfile.NamedTemporaryFile(delete=False, suffix = ".xlsx") as temp_file:
            temp_file.write(output.read())
            temp_file_path = temp_file.name

        os.startfile(temp_file_path)