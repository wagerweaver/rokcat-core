class BridgeProvider:
    def get_quote(self, token, amount, from_chain, to_chain):
        raise NotImplementedError

    def execute(self, quote):
        raise NotImplementedError

def get_all_providers():
    return [SquidProvider(), StargateProvider(), WormholeProvider()]

class SquidProvider(BridgeProvider):
    pass

class StargateProvider(BridgeProvider):
    pass

class WormholeProvider(BridgeProvider):
    pass
