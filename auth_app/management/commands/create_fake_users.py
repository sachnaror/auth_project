from auth_app.models import PlainTextPassword
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = 'Create fake users with plain text passwords'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        for _ in range(total):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()

            user = User.objects.create_user(username=username, email=email, password=password)
            PlainTextPassword.objects.create(user=user, plain_text_password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {username} with password {password}'))
