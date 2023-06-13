from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        help_text="Укажите Имя",
        db_index=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
        help_text="Укажите фамилию",
        db_index=True
    )
    patronymic = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name="Отчество",
        help_text="Укажите отчество"
    )

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ("last_name", "first_name", "patronymic")

