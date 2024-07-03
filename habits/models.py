from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):

    PERIOD_CHOICES = [
        ('daily', 'daily'),
        ('weekly', 'weekly')
    ]

    ACTION_CHOICES = [
        ('walk', 'walk outside'),
        ('drink', 'drink more water'),
        ('good_mood', 'be friendly')

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='create a habit', **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='place', **NULLABLE)
    time = models.DateTimeField(verbose_name='timestamp', **NULLABLE)
    action = models.CharField(max_length=200, choices=ACTION_CHOICES, verbose_name='action', **NULLABLE)
    is_nice = models.BooleanField(default=False, verbose_name='nice habit')
    habits = models.ForeignKey('Habit', on_delete=models.CASCADE, verbose_name='related habis', **NULLABLE)
    period = models.CharField(max_length=50, choices=PERIOD_CHOICES, verbose_name='period', **NULLABLE)
    lead_time = models.IntegerField(verbose_name='time to lead', **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name='reward', **NULLABLE)
    is_public = models.BooleanField(default=False,  verbose_name='publish')

    def __str__(self):
        return f'{self.user} - {self.action}'

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'