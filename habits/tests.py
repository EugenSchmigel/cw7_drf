from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitApiTestCase(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create(email='admin@arsolex.de', is_active=True)
        user.set_password('12345')
        user.save()
        response = self.client.post(
            '/users/token/',
            data={"email": "admin@arsolex.de", "password": "12345"})
        self.token = response.json()["access"]

        self.user = user

    def test_create_lesson(self):

        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        Habit.objects.create(
            user=self.user,
            place='Test',
            time="2024-06-01 19:23:28",
            action='good_mood',
            is_nice=False,
            period="daily",
            lead_time=30,
            is_public=True,
            reward='Test'
        )

        response = self.client.post(
            '/habits/create/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(Habit.objects.all().exists())

    def test_list_lesson(self):

        Habit.objects.create(
            user=self.user,
            place='TEst',
            time="2024-03-31 09:13:56",
            action='good_mood',
            is_nice=False,
            period="daily",
            lead_time=30,
            is_public=True,
            reward='Test'
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.get(
            '/habits/list/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_lesson(self):

        habit = Habit.objects.create(
            user=self.user,
            place='TEst',
            time="2024-07-01 16:33:19",
            action='good_mood',
            is_nice=False,
            period="daily",
            lead_time=30,
            is_public=True,
            reward='Test'
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.get(
            f'/habits/retrieve/{habit.id}/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):

        habit = Habit.objects.create(
            user=self.user,
            place='TEst',
            time="2024-04-30 10:32:29",
            action='good_mood',
            is_nice=False,
            period="daily",
            lead_time=30,
            is_public=True,
            reward='TEst'
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        data = {
            'place': 'Test update'
        }

        response = self.client.patch(
            f'/habits/update/{habit.id}/',
            data=data,
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['place'],
            'Test update'
        )

    def test_delete_lesson(self):

        habit = Habit.objects.create(
            user=self.user,
            place='Test place',
            time="2024-07-03 14:12:39",
            action='good_mood',
            is_nice=False,
            period="daily",
            lead_time=30,
            is_public=True,
            reward='Test'
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.delete(
            f'/habits/destroy/{habit.id}/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )