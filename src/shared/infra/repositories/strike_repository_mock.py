from src.shared.domain.entities.strike import Strike

class StrikeRepositoryMock:
    def __init__(self):
        self.strikes = []

    def create_strike(self, strike: Strike) -> Strike:
        self.strikes.append(strike)
        return strike

    def get_all(self) -> list[Strike]:
        return self.strikes

    def find_by_id(self, strike_id: str) -> Strike:
        for strike in self.strikes:
            if strike.id == strike_id:
                return strike
        return None

    def remove(self, strike_id: str) -> Strike:
        for strike in self.strikes:
            if strike.id == strike_id:
                self.strikes.remove(strike)
                return strike
        return None