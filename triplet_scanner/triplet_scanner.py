
class TripletScanner:
    def __init__(self, tokens, pairs, prices, liquidity, fees, historical_data=None):
        self.tokens = tokens
        self.pairs = pairs
        self.prices = prices
        self.liquidity = liquidity
        self.fees = fees
        self.historical_data = historical_data or {}
        self.routes = []

    def generate_triplets(self):
        for a in self.tokens:
            for b in self.tokens:
                for c in self.tokens:
                    if self._valid_combination(a, b, c):
                        self.routes.append((a, b, c))

    def _valid_combination(self, a, b, c):
        return (
            a != b and b != c and a != c and
            (a, b) in self.pairs and
            (b, c) in self.pairs
        )

    def validate_and_score_routes(self):
        validated = []
        for route in self.routes:
            if is_route_executable(route, self.liquidity, self.fees):
                score = score_triplet(route, self.prices, self.fees, self.historical_data)
                validated.append((route, score))
        self.routes = sorted(validated, key=lambda x: x[1], reverse=True)
