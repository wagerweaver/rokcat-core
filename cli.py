
from validator import LoopValidator
from enums import ValidationDecision
from mocks import get_mock_exchanges, get_token  # These should be created for CLI use

def run():
    buy, sell = get_mock_exchanges()
    token = get_token("ARB")
    validator = LoopValidator(buy, sell, token, 1000)
    decision, reasons = validator.validate()
    print(f"\nDecision: {decision.value}")
    if reasons:
        print("Reasons:")
        for r in reasons:
            print(f" - {r}")

if __name__ == "__main__":
    run()
