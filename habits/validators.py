from rest_framework.serializers import ValidationError

from habits.models import Habit


class HabitValidator:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        val1 = dict(value).get(self.field1)
        val2 = dict(value).get(self.field2)
        if val1 and val2:
            raise ValidationError(" Not allowed select related habit and reward")


class TimeValidator:

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        val = dict(value).get(self.field1)
        if val is not None and int(val) > 120:
            raise ValidationError("time more 120 sec.")


class ConnectedHabitValidator:

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        val1 = dict(value).get(self.field1)
        filter_list = list(Habit.objects.filter(is_nice=False).values())
        for i in filter_list:
            if val1 is not None:
                if i['id'] == val1.id:
                    raise (ValidationError
                           ("Bound habits may include. only habits with the characteristic of a pleasant habit."))


class NiceHabitValidator:

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        val1 = dict(value).get(self.field1)
        val2 = dict(value).get(self.field2)
        val3 = dict(value).get(self.field3)
        if val1 is True and (val2 is not None or val3 is not None):
            raise (ValidationError
                   ("A pleasant habit cannot have have a reward or a bound habit."))