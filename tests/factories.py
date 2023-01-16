import factory
from factory.django import DjangoModelFactory
from factory import Faker

from advertisements.models import Advertisement, Category
from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("name")
    birth_date = "2010-01-01"
    password = Faker("random_number")
    email = Faker("email")
    role = "Admin"


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = Faker("name")
    slug = Faker("ean", length=8)


class AdFactory(DjangoModelFactory):
    class Meta:
        model = Advertisement

    name = Faker("name")
    price = 1000
    description = ""
    is_published = False
    image = ""
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
