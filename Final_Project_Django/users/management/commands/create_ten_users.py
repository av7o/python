from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Create 10 users with unique emails and usernames'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            email = f'user{i}@example.com'
            username = f'user{i}'
            if not CustomUser.objects.filter(email=email).exists():
                user = CustomUser.objects.create_user(
                    email=email,
                    username=username,
                    password='avtoavto'
                )
                self.stdout.write(self.style.SUCCESS(f'Created user: {email}'))
            else:
                self.stdout.write(self.style.WARNING(f'User {email} already exists'))