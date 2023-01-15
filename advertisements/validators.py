from rest_framework.serializers import ValidationError


def check_ad_is_published(value: bool):
    """
    Проверяет значение поля 'is_published' модели 'Advertisement'
    """
    if value:
        raise ValidationError(" Поле 'is_published' не может быть 'True' ")


def check_ad_name_length(value: str):
    """
    Проверяет минимальную длину поля 'name' модели 'Advertisement'
    """
    if len(value) < 10:
        raise ValidationError(" Поле 'name' не может быть короче 10 символов ")
