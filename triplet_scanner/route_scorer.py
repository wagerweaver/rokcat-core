
def score_triplet(route, prices, fees, history):
    a, b, c = route
    spread = estimate_total_spread(a, b, c, prices)
    fee_penalty = estimate_total_fees(a, b, c, fees)
    history_boost = get_historical_boost(route, history)
    return (
        0.4 * normalize(spread) +
        0.2 * (1 - normalize(fee_penalty)) +
        0.1 * get_token_quality_score([a, b, c]) +
        0.1 * get_trade_frequency_score([a, b, c]) +
        0.2 * history_boost
    )
