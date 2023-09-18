from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name="Электронная почта",
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения",
    )
    # photo = models.ImageField(
    #     upload_to='users/%Y/%m/%d',
    #     blank=True,
    # )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=("username", "email"),
                name="unique_user"
            )
        ]
        ordering = [-'id']

    def __str__(self) -> str:
        return self.username
