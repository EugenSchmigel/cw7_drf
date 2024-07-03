from datetime import timezone, timedelta

import requests
from django.conf import settings
from habits.models import Habit


class MyBot:
    URL = "https://api.telegram.org/bot"
    TOKEN = settings.TELEGRAM_TOKEN

    def send_notification(self):
        habits = Habit.objects.all()
        # token = os.getenv('TELEGRAM_TOKEN')
        token = settings.TELEGRAM_TOKEN
        message = f"Reminder of {habits} a habit Afterwards you may: "
        send_message(token=token, message=message)


def send_message(token, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        'chat_id': '1851550460',
        'text': message
    }

    response = requests.post(url, data=data)
    return response.json()


