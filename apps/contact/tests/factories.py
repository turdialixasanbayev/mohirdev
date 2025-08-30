import factory
from factory.django import DjangoModelFactory
from apps.contact.models import ContactUs


class ContactUsFactory(DjangoModelFactory):
    """
    Factory for creating ContactUs model instances in tests.
    Uses Faker for generating realistic test data.
    """

    class Meta:
        model = ContactUs

    name = factory.Faker("name")
    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    link = factory.Faker("url")
    subject = factory.Faker("sentence", nb_words=4)
    message = factory.Faker("paragraph")


class InactiveContactUsFactory(ContactUsFactory):
    """
    Factory for creating inactive ContactUs model instances in tests.
    """

    is_active = False
