from src.modules.batch_get_member.app.batch_get_member_usecase import BatchGetMemberUsecase
from src.modules.batch_get_member.app.batch_get_member_viewmodel import BatchGetMemberViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_BatchGetMemberViewmodel:
    def test_batch_get_member_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        members = usecase(ras=[repo.members[0].ra, repo.members[1].ra])
        viewmodel = BatchGetMemberViewmodel(members).to_dict()

        expected = {
            'members': [
                {
                    'name': 'Vitor Guirão MPNTM',
                    'email_dev': 'vsoller.devmaua@gmail.com',
                    'email': 'vsoller@airubio.com',
                    'ra': '21017310',
                    'role': 'DIRECTOR',
                    'stack': 'INFRA',
                    'year': 1,
                    'cellphone': '11991758098',
                    'course': 'ECA',
                    'hired_date': 1634576165000,
                    'deactivated_date': None,
                    'active': 'ACTIVE'
                },
                {
                    'name': 'Joao Branco',
                    'email_dev': 'jbranco.devmaua@gmail.com',
                    'email': 'jbranco@gmail.com',
                    'ra': '21010757',
                    'role': 'HEAD',
                    'stack': 'BACKEND',
                    'year': 3,
                    'cellphone': '11991152348',
                    'course': 'ECM',
                    'hired_date': 1634921765000,
                    'deactivated_date': None,
                    'active': 'ACTIVE'
                }
            ],
            'message': 'the members were retrieved'
        }

        assert viewmodel == expected