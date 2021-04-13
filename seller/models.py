from django.contrib.auth.models import AbstractUser


"""
Модель пользователей
"""


class User(AbstractUser):
    def __str__(self):
        return f"<User {self.username} />"
