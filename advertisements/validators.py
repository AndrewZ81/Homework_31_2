from rest_framework.serializers import ValidationError


def check_ad_is_published(value: bool):
    """
    Проверяет значение поля 'is_published' модели 'Advertisement'
    """
    if value:
        raise ValidationError("Значение не может быть 'True'")
