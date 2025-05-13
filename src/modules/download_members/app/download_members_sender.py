import datetime
from download_members_extractor import DownloadMembersExtractor
from download_members_transformer import DownloadMembersTransformer
from src.shared.environments import Environments
from src.shared.infra.repositories import S3Manager


repo = Environments.get_envs().get_member_repo()()

def lambda_handler(event,context):
    extractor = DownloadMembersExtractor(repo)

    current_date = datetime.datetime.now()

    year = current_date.year
    month = current_date.month
    day = current_date.day

    file_name = f"relatorio_gerado_em_{day}_{month}_{year}.xlsx"
    file_path = f"relatorios/"

    extractor = DownloadMembersExtractor(member_repository=repo)
    transformer = DownloadMembersTransformer(extractor)
    download = transformer()

    if download:

        bucket_manager = S3Manager()

        try:

            response = bucket_manager.upload_file(key=file_path + file_name,
                                                   file_type=".xlsx",
                                                   decode_string=download,
                                                   )
            if response.get('s3_response', {}).get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
                print("Download generated and uploaded successfully")
                return {
                    "statusCode": 200,
                    "body": f"File {file_name} successfully uploaded to S3."
                }
            else:
                print("Error uploading file to S3")
                return {
                    "statusCode": 500,
                    "body": "Error uploading file to S3"
                }
        except Exception as e:
            print(f"Error: {str(e)}")
            raise Exception("Error uploading file to S3")
        
    else:

        raise Exception("Error generating download")