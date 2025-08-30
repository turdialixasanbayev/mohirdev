import pytest
from django.urls import reverse
from rest_framework import status
from apps.contact.models import ContactUs
from apps.contact.tests.factories import ContactUsFactory, InactiveContactUsFactory


@pytest.mark.django_db
class TestContactUsAPI:
    """
    Test suite for the Contact Us API endpoints.
    """

    def test_create_contact(self, client):
        """
        Test creating a new contact.
        """

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

    def test_list_contacts(self, client, contact):
        url = reverse("contacts-list")
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK

        results = response.data["results"]
        assert results[0]["email"] == contact.email

    def test_retrieve_contact(self, client, contact):
        url = reverse("contacts-detail", args=[contact.pk])
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == contact.email

    def test_update_contact(self, client, contact):
        url = reverse("contacts-detail", args=[contact.pk])
        response = client.patch(
            url, {"subject": "Updated subject"}, format="json")

        assert response.status_code == status.HTTP_200_OK
        contact.refresh_from_db()
        assert contact.subject == "Updated subject"

    def test_soft_delete_contact(self, client, contact):
        url = reverse("contacts-detail", args=[contact.pk])
        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        contact.refresh_from_db()
        assert contact.is_active is False

    # def test_list_contacts_only_active(self, client):
    #     # 1 ta aktiv va 1 ta inaktiv contact yaratamiz
    #     active_contact = ContactUsFactory()
    #     inactive_contact = InactiveContactUsFactory()

    #     url = reverse("contacts-list")
    #     response = client.get(url)

    #     assert response.status_code == status.HTTP_200_OK
    #     results = response.data["results"]

    #     # Faqat active contact chiqishi kerak
    #     emails = [r["email"] for r in results]
    #     assert active_contact.email in emails
    #     assert inactive_contact.email not in emails

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
