class SignalFilter:
    def __init__(self, config, scorer):
        self.config = config
        self.scorer = scorer

    def validate(self, signal):
        score = self.scorer.score(signal)
        return score >= self.config["min_score"]
