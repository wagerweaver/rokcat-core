
from ..validator import LoopValidator
from ..enums import ValidationDecision

def test_validator_passes_basic_case():
    buy = MockExchange(...)  # Replace with mock or stub implementation
    sell = MockExchange(...)
    token = MockToken(...)
    validator = LoopValidator(buy, sell, token, 1000)
    decision, reasons = validator.validate()
    assert decision == ValidationDecision.PROCEED
    assert not reasons
