import datetime
from dateutil import relativedelta
from rest_framework.serializers import ValidationError


def check_user_age(value):
    """
    Проверяет значение поля 'birth_date' модели 'User'
    """
    user_age = relativedelta(datetime.date.today(), value).years
    if user_age < 9:
        raise ValidationError("Возраст не может быть меньше 9 лет")
