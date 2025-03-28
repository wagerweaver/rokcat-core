class Notifier:
    def __init__(self, webhook):
        self.webhook = webhook

    def notify(self, message):
        print(f"[ALERT] {message}")
        # Future: post to Slack/Telegram webhook
