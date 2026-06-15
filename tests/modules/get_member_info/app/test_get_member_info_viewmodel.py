from src.modules.get_member_info.app.get_member_info_usecase import GetMemberInfoUsecase
from src.modules.get_member_info.app.get_member_info_viewmodel import GetMemberInfoViewModel
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from pprint import pprint


class Test_GetMemberInfoViewModel:
    def test_get_member_info_viewmodel(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = GetMemberInfoUsecase(member_repo, action_repo)

        # Vitor Guirão solicitando
        members = usecase(requester_user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3')
        viewmodel = GetMemberInfoViewModel(members=members).to_dict()

        pprint(viewmodel)

        # Verifica se as listas principais foram criadas
        assert 'ALL' in viewmodel
        assert type(viewmodel['ALL']) == list
        assert len(viewmodel['ALL']) == len(members)

        # Verifica se agrupou pelas stacks que existem no mock (ex: BACKEND, FRONTEND, INFRA)
        # O mock tem membros dessas stacks
        assert 'BACKEND' in viewmodel
        assert 'FRONTEND' in viewmodel
        assert 'INFRA' in viewmodel

        # Validando a estrutura de um membro dentro da lista ALL
        vitor = next((m for m in viewmodel['ALL'] if m['name'] == 'Vitor Guirão MPNTM'), None)
        assert vitor is not None
        assert vitor['ra'] == '21017310'
        assert vitor['role'] == 'DIRECTOR'
        assert vitor['stack'] == 'INFRA'
        assert vitor['year'] == 1
        assert vitor['course'] == 'ECA'
        assert type(vitor['project']) == list
        assert vitor['hired_date'] == 1634576165000
        assert vitor['photo'] is None

    def test_get_member_info_viewmodel_empty_list(self):
        # Testa como o viewmodel se comporta caso o repositório retorne vazio
        viewmodel = GetMemberInfoViewModel(members=[]).to_dict()

        assert 'ALL' in viewmodel
        assert len(viewmodel['ALL']) == 0
        assert len(viewmodel.keys()) == 1 # Somente a chave ALL deve existir