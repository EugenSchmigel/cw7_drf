from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitRetrieveAPIView,HabitDestroyAPIView,HabitListAPIView, HabitPublicAPIView,HabitUpdateAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('retrieve/<int:pk>/', HabitRetrieveAPIView.as_view(),name='retrieve_habit'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('destroy/<int:pk>/', HabitDestroyAPIView.as_view(),name='destroy_habit'),
    path('list/', HabitListAPIView.as_view(), name='list_habit'),
    path('list_public/', HabitPublicAPIView.as_view(),name='list_habit_public')

    ]
