import smtplib
import requests

class AlertManager:
    def __init__(self, price_threshold=None, telegram_token=None):
        self.price_threshold = price_threshold
        self.telegram_token = telegram_token

    def check_price(self, current_price):
        if self.price_threshold and current_price >= self.price_threshold:
            print(f"Price alert triggered: {current_price} >= {self.price_threshold}")
            self.send_email_alert(current_price)

    def send_email_alert(self, current_price):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("goutam.vivek.4@gmail.com", "vivek@1978")
            subject = f"Crypto Price crossed threshold : {current_price}"
            server.sendmail("goutam.vivek.4@gmail.com", "goutam.vivek@gmail.com", subject)
            server.quit()
        except Exception as e:
            print(f"Failed to send email alert: {e}")




