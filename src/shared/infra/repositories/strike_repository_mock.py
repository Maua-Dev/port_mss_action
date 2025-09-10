from src.shared.domain.repositories.strike_repository_interface import IStrikeRepository
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from typing import List, Optional


class StrikeRepositoryMock(IStrikeRepository):
    def __init__(self):
        # 20 exemplos de strikes
               self.strikes = [
            Strike(
                strike_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1703980800000,  # 2023-12-30
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Comportamento inadequado durante reunião"
            ),
            Strike(
                strike_id="b2c3d4e5-f6g7-8901-2345-678901bcdefg",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1704067200000,  # 2023-12-31
                category=STRIKE_CATEGORY.LACK_OF_COMMITMENT,
                description="Ausência injustificada em projeto crítico"
            ),
            Strike(
                strike_id="c3d4e5f6-g7h8-9012-3456-789012cdefgh",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1704153600000,  # 2024-01-01
                category=STRIKE_CATEGORY.RULE_VIOLATION,
                description="Violação das políticas de segurança da informação"
            ),
            Strike(
                strike_id="d4e5f6g7-h8i9-0123-4567-890123defghi",
                owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                target_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1704240000000,  # 2024-01-02
                category=STRIKE_CATEGORY.OTHER,
                description="Uso inadequado de recursos da empresa"
            ),
            Strike(
                strike_id="e5f6g7h8-i9j0-1234-5678-901234efghij",
                owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                target_user_id="76h35dg4-h76v-1875-987hn-h67gfv45Gt4",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1704326400000,  # 2024-01-03
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Linguagem inapropriada com colegas"
            ),
            Strike(
                strike_id="f6g7h8i9-j0k1-2345-6789-012345fghijk",
                owner_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1704412800000,  # 2024-01-04
                category=STRIKE_CATEGORY.LACK_OF_COMMITMENT,
                description="Não cumprimento de prazos estabelecidos"
            ),
            Strike(
                strike_id="g7h8i9j0-k1l2-3456-7890-123456ghijkl",
                owner_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                target_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1704499200000,  # 2024-01-05
                category=STRIKE_CATEGORY.RULE_VIOLATION,
                description="Acesso não autorizado a sistemas"
            ),
            Strike(
                strike_id="h8i9j0k1-l2m3-4567-8901-234567hijklm",
                owner_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                target_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1704585600000,  # 2024-01-06
                category=STRIKE_CATEGORY.OTHER,
                description="Descumprimento do código de conduta"
            ),
            Strike(
                strike_id="i9j0k1l2-m3n4-5678-9012-345678ijklmn",
                owner_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                target_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1704672000000,  # 2024-01-07
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Conflito de interesses não declarado"
            ),
            Strike(
                strike_id="j0k1l2m3-n4o5-6789-0123-456789jklmno",
                owner_user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                target_user_id="3b07232f-4f65-42c6-b005-242550b8b8dc",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                occurred_date=1704758400000,  # 2024-01-08
                category=STRIKE_CATEGORY.LACK_OF_COMMITMENT,
                description="Baixa qualidade nas entregas"
            ),
            Strike(
                strike_id="k1l2m3n4-o5p6-7890-1234-567890klmnop",
                owner_user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                target_user_id="5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                occurred_date=1704844800000,  # 2024-01-09
                category=STRIKE_CATEGORY.RULE_VIOLATION,
                description="Compartilhamento indevido de informações confidenciais"
            ),
            Strike(
                strike_id="l2m3n4o5-p6q7-8901-2345-678901lmnopq",
                owner_user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                target_user_id="9183jBnh-997H-1010-10god-914gHy46tBh",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                occurred_date=1704931200000,  # 2024-01-10
                category=STRIKE_CATEGORY.OTHER,
                description="Negligência na manutenção de equipamentos"
            ),
            Strike(
                strike_id="m3n4o5p6-q7r8-9012-3456-789012mnopqr",
                owner_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                target_user_id="75648hbr-184n-1985-91han-7ghn4HgF182",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                occurred_date=1705017600000,  # 2024-01-11
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Discriminação no ambiente de trabalho"
            ),
            Strike(
                strike_id="n4o5p6q7-r8s9-0123-4567-890123nopqrs",
                owner_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                target_user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                occurred_date=1705104000000,  # 2024-01-12
                category=STRIKE_CATEGORY.LACK_OF_COMMITMENT,
                description="Falta de participação em treinamentos obrigatórios"
            ),
            Strike(
                strike_id="o5p6q7r8-s9t0-1234-5678-901234opqrst",
                owner_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                target_user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                occurred_date=1705190400000,  # 2024-01-13
                category=STRIKE_CATEGORY.RULE_VIOLATION,
                description="Uso pessoal excessivo de recursos corporativos"
            ),
            Strike(
                strike_id="p6q7r8s9-t0u1-2345-6789-012345pqrstu",
                owner_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
                target_user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                occurred_date=1705276800000,  # 2024-01-14
                category=STRIKE_CATEGORY.OTHER,
                description="Falha na documentação de processos críticos"
            ),
            Strike(
                strike_id="q7r8s9t0-u1v2-3456-7890-123456qrstuv",
                owner_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                target_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                occurred_date=1705363200000,  # 2024-01-15
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Assédio moral reportado por múltiplas pessoas"
            ),
            Strike(
                strike_id="r8s9t0u1-v2w3-4567-8901-234567rstuvw",
                owner_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                target_user_id="76h35dg4-h76v-1875-987hn-h67gfv45Gt4",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                occurred_date=1705449600000,  # 2024-01-16
                category=STRIKE_CATEGORY.LACK_OF_COMMITMENT,
                description="Abandono de responsabilidades sem notificação"
            ),
            Strike(
                strike_id="s9t0u1v2-w3x4-5678-9012-345678stuvwx",
                owner_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                occurred_date=1705536000000,  # 2024-01-17
                category=STRIKE_CATEGORY.RULE_VIOLATION,
                description="Violação das normas de saúde e segurança"
            ),
            Strike(
                strike_id="t0u1v2w3-x4y5-6789-0123-456789tuvwxy",
                owner_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                target_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
                occurred_date=1705622400000,  # 2024-01-18
                category=STRIKE_CATEGORY.OTHER,
                description="Insubordinação repetida às orientações da liderança"
            )
        ]


    def create_strike(self, strike: Strike) -> Strike:
        self.strikes.append(strike)
        return strike

    def get_all(self) -> list[Strike]:
        return self.strikes.copy()

    def find_by_id(self, strike_id: str) -> Optional[Strike]:
        if not strike_id:
            return None

        for strike in self.strikes:
            if strike.strike_id == strike_id:
                return strike
        return None

    def get_strike(self, strike_id: str) -> Optional[Strike]:
        return self.find_by_id(strike_id)

    def delete_strike(self, strike_id: str) -> Optional[Strike]:
        if not strike_id:
            return None

        for i, strike in enumerate(self.strikes):
            if strike.strike_id == strike_id:
                return self.strikes.pop(i)
        return None