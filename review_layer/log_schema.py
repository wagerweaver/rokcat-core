def format_log(event_type, timestamp, token, route, spread, fees, outcome, notes):
    return {
        "Type": event_type,
        "Timestamp": timestamp,
        "Token": token,
        "Route": route,
        "Spread": spread,
        "Fees": fees,
        "Outcome": outcome,
        "Notes": notes
    }
