from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

User = get_user_model()

class Command(BaseCommand):
    help = 'Create 10 fake users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            User.objects.create_user(
                username=fake.user_name(),
                password='password123',
                email=fake.email()
            )
        self.stdout.write(self.style.SUCCESS('Successfully created 10 fake users'))
