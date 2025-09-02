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
                owner_user_id="12345678-1234-1234-1234-123456789abc",
                target_user_id="87654321-4321-4321-4321-cba987654321",
                applier_user_id="11111111-2222-3333-4444-555555555555",
                ocurred_date=1703980800000,  # 2023-12-30
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Comportamento inadequado durante reunião"
            ),
            Strike(
                strike_id="b2c3d4e5-f6g7-8901-2345-678901bcdefg",
                owner_user_id="23456789-2345-2345-2345-23456789abcd",
                target_user_id="98765432-5432-5432-5432-dcba98765432",
                applier_user_id="22222222-3333-4444-5555-666666666666",
                ocurred_date=1704067200000,  # 2023-12-31
                category=STRIKE_CATEGORY.LACK_OF_COMMITMENT,
                description="Ausência injustificada em projeto crítico"
            ),
            Strike(
                strike_id="c3d4e5f6-g7h8-9012-3456-789012cdefgh",
                owner_user_id="34567890-3456-3456-3456-3456789abcde",
                target_user_id="09876543-6543-6543-6543-edcb09876543",
                applier_user_id="33333333-4444-5555-6666-777777777777",
                ocurred_date=1704153600000,  # 2024-01-01
                category=STRIKE_CATEGORY.RULE_VIOLATION,
                description="Violação das políticas de segurança da informação"
            ),
            Strike(
                strike_id="d4e5f6g7-h8i9-0123-4567-890123defghi",
                owner_user_id="45678901-4567-4567-4567-456789abcdef",
                target_user_id="19876543-7654-7654-7654-fedc19876543",
                applier_user_id="44444444-5555-6666-7777-888888888888",
                ocurred_date=1704240000000,  # 2024-01-02
                category=STRIKE_CATEGORY.OTHER,
                description="Uso inadequado de recursos da empresa"
            ),
            Strike(
                strike_id="e5f6g7h8-i9j0-1234-5678-901234efghij",
                owner_user_id="56789012-5678-5678-5678-56789abcdefg",
                target_user_id="29876543-8765-8765-8765-gfed29876543",
                applier_user_id="55555555-6666-7777-8888-999999999999",
                ocurred_date=1704326400000,  # 2024-01-03
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Linguagem inapropriada com colegas"
            ),
            Strike(
                strike_id="f6g7h8i9-j0k1-2345-6789-012345fghijk",
                owner_user_id="67890123-6789-6789-6789-6789abcdefgh",
                target_user_id="39876543-9876-9876-9876-hgfe39876543",
                applier_user_id="66666666-7777-8888-9999-aaaaaaaaaaaa",
                ocurred_date=1704412800000,  # 2024-01-04
                category=STRIKE_CATEGORY.LACK_OF_COMMITMENT,
                description="Não cumprimento de prazos estabelecidos"
            ),
            Strike(
                strike_id="g7h8i9j0-k1l2-3456-7890-123456ghijkl",
                owner_user_id="78901234-7890-7890-7890-789abcdefghi",
                target_user_id="49876543-0987-0987-0987-ihgf49876543",
                applier_user_id="77777777-8888-9999-aaaa-bbbbbbbbbbbb",
                ocurred_date=1704499200000,  # 2024-01-05
                category=STRIKE_CATEGORY.RULE_VIOLATION,
                description="Acesso não autorizado a sistemas"
            ),
            Strike(
                strike_id="h8i9j0k1-l2m3-4567-8901-234567hijklm",
                owner_user_id="89012345-8901-8901-8901-89abcdefghij",
                target_user_id="59876543-1098-1098-1098-jihg59876543",
                applier_user_id="88888888-9999-aaaa-bbbb-cccccccccccc",
                ocurred_date=1704585600000,  # 2024-01-06
                category=STRIKE_CATEGORY.OTHER,
                description="Descumprimento do código de conduta"
            ),
            Strike(
                strike_id="i9j0k1l2-m3n4-5678-9012-345678ijklmn",
                owner_user_id="90123456-9012-9012-9012-9abcdefghijk",
                target_user_id="69876543-2109-2109-2109-kjih69876543",
                applier_user_id="99999999-aaaa-bbbb-cccc-dddddddddddd",
                ocurred_date=1704672000000,  # 2024-01-07
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Conflito de interesses não declarado"
            ),
            Strike(
                strike_id="j0k1l2m3-n4o5-6789-0123-456789jklmno",
                owner_user_id="01234567-0123-0123-0123-abcdefghijkl",
                target_user_id="79876543-3210-3210-3210-lkjh79876543",
                applier_user_id="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                ocurred_date=1704758400000,  # 2024-01-08
                category=STRIKE_CATEGORY.LACK_OF_COMMITMENT,
                description="Baixa qualidade nas entregas"
            ),
            Strike(
                strike_id="k1l2m3n4-o5p6-7890-1234-567890klmnop",
                owner_user_id="12345678-1234-5678-9012-bcdefghijklm",
                target_user_id="89876543-4321-4321-4321-mlkj89876543",
                applier_user_id="bbbbbbbb-cccc-dddd-eeee-ffffffffffff",
                ocurred_date=1704844800000,  # 2024-01-09
                category=STRIKE_CATEGORY.RULE_VIOLATION,
                description="Compartilhamento indevido de informações confidenciais"
            ),
            Strike(
                strike_id="l2m3n4o5-p6q7-8901-2345-678901lmnopq",
                owner_user_id="23456789-2345-6789-0123-cdefghijklmn",
                target_user_id="99876543-5432-5432-5432-nmlk99876543",
                applier_user_id="cccccccc-dddd-eeee-ffff-gggggggggggg",
                ocurred_date=1704931200000,  # 2024-01-10
                category=STRIKE_CATEGORY.OTHER,
                description="Negligência na manutenção de equipamentos"
            ),
            Strike(
                strike_id="m3n4o5p6-q7r8-9012-3456-789012mnopqr",
                owner_user_id="34567890-3456-7890-1234-defghijklmno",
                target_user_id="09876543-6543-6543-6543-onml09876543",
                applier_user_id="dddddddd-eeee-ffff-gggg-hhhhhhhhhhhh",
                ocurred_date=1705017600000,  # 2024-01-11
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Discriminação no ambiente de trabalho"
            ),
            Strike(
                strike_id="n4o5p6q7-r8s9-0123-4567-890123nopqrs",
                owner_user_id="45678901-4567-8901-2345-efghijklmnop",
                target_user_id="19876543-7654-7654-7654-ponm19876543",
                applier_user_id="eeeeeeee-ffff-gggg-hhhh-iiiiiiiiiiii",
                ocurred_date=1705104000000,  # 2024-01-12
                category=STRIKE_CATEGORY.LACK_OF_COMMITMENT,
                description="Falta de participação em treinamentos obrigatórios"
            ),
            Strike(
                strike_id="o5p6q7r8-s9t0-1234-5678-901234opqrst",
                owner_user_id="56789012-5678-9012-3456-fghijklmnopq",
                target_user_id="29876543-8765-8765-8765-qpon29876543",
                applier_user_id="ffffffff-gggg-hhhh-iiii-jjjjjjjjjjjj",
                ocurred_date=1705190400000,  # 2024-01-13
                category=STRIKE_CATEGORY.RULE_VIOLATION,
                description="Uso pessoal excessivo de recursos corporativos"
            ),
            Strike(
                strike_id="p6q7r8s9-t0u1-2345-6789-012345pqrstu",
                owner_user_id="67890123-6789-0123-4567-ghijklmnopqr",
                target_user_id="39876543-9876-9876-9876-rqpo39876543",
                applier_user_id="gggggggg-hhhh-iiii-jjjj-kkkkkkkkkkkk",
                ocurred_date=1705276800000,  # 2024-01-14
                category=STRIKE_CATEGORY.OTHER,
                description="Falha na documentação de processos críticos"
            ),
            Strike(
                strike_id="q7r8s9t0-u1v2-3456-7890-123456qrstuv",
                owner_user_id="78901234-7890-1234-5678-hijklmnopqrs",
                target_user_id="49876543-0987-0987-0987-srqp49876543",
                applier_user_id="hhhhhhhh-iiii-jjjj-kkkk-llllllllllll",
                ocurred_date=1705363200000,  # 2024-01-15
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Assédio moral reportado por múltiplas pessoas"
            ),
            Strike(
                strike_id="r8s9t0u1-v2w3-4567-8901-234567rstuvw",
                owner_user_id="89012345-8901-2345-6789-ijklmnopqrst",
                target_user_id="59876543-1098-1098-1098-tsrq59876543",
                applier_user_id="iiiiiiii-jjjj-kkkk-llll-mmmmmmmmmmmm",
                ocurred_date=1705449600000,  # 2024-01-16
                category=STRIKE_CATEGORY.LACK_OF_COMMITMENT,
                description="Abandono de responsabilidades sem notificação"
            ),
            Strike(
                strike_id="s9t0u1v2-w3x4-5678-9012-345678stuvwx",
                owner_user_id="90123456-9012-3456-7890-jklmnopqrstu",
                target_user_id="69876543-2109-2109-2109-utsr69876543",
                applier_user_id="jjjjjjjj-kkkk-llll-mmmm-nnnnnnnnnnnn",
                ocurred_date=1705536000000,  # 2024-01-17
                category=STRIKE_CATEGORY.RULE_VIOLATION,
                description="Violação das normas de saúde e segurança"
            ),
            Strike(
                strike_id="t0u1v2w3-x4y5-6789-0123-456789tuvwxy",
                owner_user_id="01234567-0123-4567-8901-klmnopqrstuv",
                target_user_id="79876543-3210-3210-3210-vuts79876543",
                applier_user_id="kkkkkkkk-llll-mmmm-nnnn-oooooooooooo",
                ocurred_date=1705622400000,  # 2024-01-18
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

    def delete_strike(self, strike_id: str) -> Optional[Strike]:
        if not strike_id:
            return None
            
        for i, strike in enumerate(self.strikes):
            if strike.strike_id == strike_id:
                return self.strikes.pop(i)
        return None