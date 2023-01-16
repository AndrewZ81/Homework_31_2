from django.db.models import Model, CharField, ManyToManyField, \
    PositiveSmallIntegerField, DecimalField, DateField, EmailField, TextChoices
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from users.validators import check_user_age


class Location(Model):

    class Meta:
        verbose_name = "Месторасположение"
        verbose_name_plural = "Месторасположения"

    def __str__(self):
        return self.name

    name = CharField(max_length=200)
    lat = DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = DecimalField(max_digits=8, decimal_places=6, null=True)


class UserRole(TextChoices):
    MEMBER = "Member", _("member")
    MODERATOR = "Moderator", _("moderator")
    ADMIN = "Admin", _("admin")


class User(AbstractUser):

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    first_name = CharField(max_length=200, null=True)
    last_name = CharField(max_length=200, null=True)
    username = CharField(max_length=200, unique=True)
    password = CharField(max_length=200)
    role = CharField(max_length=9, choices=UserRole.choices)
    age = PositiveSmallIntegerField(null=True)
    location = ManyToManyField(Location)
    birth_date = DateField(validators=[check_user_age])
    email = EmailField(unique=True, validators=[RegexValidator(
        regex="@rambler.ru",
        inverse_match=True,
        message="Регистрация с домена 'rambler.ru' запрещена"
    )])
