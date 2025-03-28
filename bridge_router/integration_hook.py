from bridge_router import BridgeRouter
from bridge_providers import get_all_providers
from latency_tracker import LatencyDB
from bridge_config import BRIDGE_CONFIG

router = BridgeRouter(get_all_providers(), LatencyDB(), BRIDGE_CONFIG)
tx_result = router.execute("USDC", 1000, "Polygon", "Ethereum")
print(tx_result)
