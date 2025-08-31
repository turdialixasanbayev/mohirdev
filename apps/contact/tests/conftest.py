import pytest
from rest_framework.test import APIClient
from apps.contact.tests.factories import ContactUsFactory


@pytest.fixture
def contact():
    """
    Creates a single active ContactUs instance for tests.
    """
    return ContactUsFactory()

@pytest.fixture
def client():
    """
    Creates a REST framework API client for tests.
    """
    return APIClient()
