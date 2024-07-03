from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView)

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.permissions import IsAutor
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitRetrieveAPIView(RetrieveAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAutor]


class HabitUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAutor]


class HabitDestroyAPIView(DestroyAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAutor]


class HabitListAPIView(ListAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAutor]


class HabitPublicAPIView(ListAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)