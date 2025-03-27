
def estimate_total_spread(a, b, c, prices):
    # Placeholder: actual logic depends on price structure
    return prices.get((a, b), 1) * prices.get((b, c), 1)

def estimate_total_fees(a, b, c, fees):
    return fees.get((a, b), 0) + fees.get((b, c), 0)

def normalize(value):
    return min(value / 100, 1)

def get_token_quality_score(tokens):
    return 0.8  # placeholder

def get_trade_frequency_score(tokens):
    return 0.6  # placeholder

def get_historical_boost(route, history):
    return history.get(route, {}).get("boost", 0.1)
