import pytest
from rest_framework.test import APIClient
from apps.contact.tests.factories import ContactUsFactory


@pytest.fixture(scope="function")
def api_client():
    """
    DRF APIClient instance for making API requests.
    """

    return APIClient()


@pytest.fixture(scope="function")
def contact():
    """
    Creates a single ContactUs instance using FactoryBoy.
    """

    return ContactUsFactory()
