import pytest
import json
from django.urls import reverse
from rest_framework import status
from apps.contact.models import ContactUs
from apps.contact.tests.factories import InactiveContactUsFactory, ContactUsFactory


@pytest.mark.django_db
class TestContactUsAPI:
    """
    Integration-level test suite for ContactUs API endpoints.
    Uses DRF APIClient and FactoryBoy for test data.
    """

    # --- CREATE ---
    def test_create_contact(self, client):
        data = {
            "name": "Turdiali",
            "email": "turdiali@example.com",
            "phone_number": "+998901234567",
            "link": "https://example.com",
            "subject": "Django testing",
            "message": "Salom! Bu test uchun yozildi.",
        }
        url = reverse("contacts-list")
        response = client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert ContactUs.objects.filter(email="turdiali@example.com").exists()

    # --- LIST ---
    def test_list_contacts(self, client, contact):
        url = reverse("contacts-list")
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        results = response.data["results"]
        assert results[0]["email"] == contact.email

    # --- RETRIEVE ---
    def test_retrieve_contact(self, client, contact):
        url = reverse("contacts-detail", args=[contact.pk])
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == contact.email

    # --- UPDATE ---
    def test_update_contact(self, client, contact):
        url = reverse("contacts-detail", args=[contact.pk])
        response = client.patch(
            url,
            data=json.dumps({"subject": "Updated subject"}),
            content_type="application/json"
        )

        assert response.status_code == status.HTTP_200_OK
        contact.refresh_from_db()
        assert contact.subject == "Updated subject"

    # --- SOFT DELETE ---
    def test_soft_delete_contact(self, client, contact):
        url = reverse("contacts-detail", args=[contact.pk])
        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        contact.refresh_from_db()
        assert contact.is_active is False

    # --- NEGATIVE TESTS ---
    def test_retrieve_not_found(self, client):
        url = reverse("contacts-detail", args=[999])
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_create_invalid_email(self, client):
        data = {
            "name": "Invalid Email User",
            "email": "invalid-email",
            "phone_number": "+998901234567",
            "subject": "Bad email",
            "message": "This should fail",
        }
        url = reverse("contacts-list")
        response = client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "email" in response.data

    # --- LIST ONLY ACTIVE CONTACTS ---
    def test_list_only_active_contacts(self, client):
        active_contact = ContactUsFactory()
        inactive_contact = InactiveContactUsFactory()

        url = reverse("contacts-list")
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        emails = [r["email"] for r in response.data["results"]]
        assert active_contact.email in emails
        assert inactive_contact.email not in emails
