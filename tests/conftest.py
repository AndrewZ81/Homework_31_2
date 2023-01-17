from pytest_factoryboy import register

from tests.factories import AdFactory, CategoryFactory, UserFactory, LocationFactory

pytest_plugins = "tests.fixtures"

register(AdFactory)
register(CategoryFactory)
register(UserFactory)
register(LocationFactory)
