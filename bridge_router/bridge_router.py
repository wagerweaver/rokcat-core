class BridgeRouter:
    def __init__(self, providers, latency_db, config):
        self.providers = providers
        self.latency_db = latency_db
        self.config = config

    def get_best_quote(self, token, amount, from_chain, to_chain):
        quotes = [p.get_quote(token, amount, from_chain, to_chain) for p in self.providers]
        return QuoteEngine.rank(quotes, self.latency_db)[0]

    def execute(self, token, amount, from_chain, to_chain):
        quote = self.get_best_quote(token, amount, from_chain, to_chain)
        try:
            return quote.provider.execute(quote)
        except Exception:
            return self.fallback_execute(token, amount, from_chain, to_chain)

    def fallback_execute(self, token, amount, from_chain, to_chain):
        fallback_quotes = QuoteEngine.rank_fallbacks(self.providers, token, amount, from_chain, to_chain)
        for quote in fallback_quotes:
            try:
                return quote.provider.execute(quote)
            except Exception:
                continue
        raise BridgeError("All fallback routes failed")
