
MIN_LIQUIDITY = 10000

def is_route_executable(route, liquidity, fees):
    a, b, c = route
    for leg in [(a, b), (b, c)]:
        if liquidity.get(leg, 0) < MIN_LIQUIDITY:
            return False
    return True
