from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='member@arsolex.de',
            first_name='MemberFN',
            last_name='MemberFN',
            is_staff=False,
            is_superuser=False,
            is_active = True

        )

        user.set_password('12345')
        user.save()