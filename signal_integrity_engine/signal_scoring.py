class SignalScorer:
    def __init__(self, trust_map, max_spread):
        self.trust_map = trust_map
        self.max_spread = max_spread

    def score(self, signal):
        spread = signal["spread"]
        token = signal["token"]
        depth = signal["depth"]

        trust_score = self.trust_map.get(token, 0.5)
        volatility_penalty = 0.2 if spread > self.max_spread else 0

        return (trust_score * 0.5) + (depth * 0.3) - volatility_penalty
