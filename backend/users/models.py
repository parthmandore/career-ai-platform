from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    college = models.CharField(
        max_length=200,
        blank=True
    )

    branch = models.CharField(
        max_length=100,
        blank=True
    )

    graduation_year = models.IntegerField(
        null=True,
        blank=True
    )

    target_company = models.CharField(
        max_length=100,
        blank=True
    )

    skills = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.user.username