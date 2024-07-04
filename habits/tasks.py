import os
from celery import shared_task
from datetime import timedelta

from django.utils import timezone

from habits.models import Habit
from habits.services import send_message


@shared_task
def send_notification():
    time_now = timezone.now()
    habits = Habit.objects.all()
    token = os.getenv('TELEGRAM_TOKEN')
    for habit in habits:
        if habit.time >= time_now - timedelta(minutes=1):
            message = f"Reminder of a habit {habit.action} Afterwards you may: {habit.habits if habit.habits else habit.reward}"
            send_message(token=token, message=message)
