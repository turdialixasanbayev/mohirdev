from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.category.models import Tag


class TestTagLCView(APITestCase):
    """
    Test suite for the Tag List/Create API view.
    """

    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_list_active_tags(self):
        url = reverse('tag-lc')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tag_names = [t["name"] for t in response.data["results"]]

        self.assertIn(self.tag.name, tag_names)

    def test_create_tag(self):
        url = reverse("tag-lc")
        data = {"name": "New Tag"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())


class TestTagRudView(APITestCase):
    """
    Test suite for the Tag Retrieve/Update/Delete API view.
    """

    def setUp(self):
        self.active_tag = Tag.objects.create(name="Active Tag", is_active=True)
        self.inactive_tag = Tag.objects.create(
            name="Inactive Tag", is_active=False)

    def test_retrieve_active_tag(self):
        url = reverse("tag-rud", args=[self.active_tag.slug])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.active_tag.name)

    def test_update_active_tag(self):
        url = reverse("tag-rud", args=[self.active_tag.slug])
        data = {"name": "Updated Tag"}
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.active_tag.refresh_from_db()
        self.assertEqual(self.active_tag.name, "Updated Tag")
        self.assertEqual(response.data["name"], "Updated Tag")

    def test_delete_active_tag(self):
        url = reverse("tag-rud", args=[self.active_tag.slug])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Soft-delete holatini tekshiramiz
        self.active_tag.refresh_from_db()
        self.assertFalse(self.active_tag.is_active)

    def test_retrieve_inactive_tag(self):
        url = reverse("tag-rud", args=[self.inactive_tag.slug])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_inactive_tag(self):
        url = reverse("tag-rud", args=[self.inactive_tag.slug])
        data = {"name": "Updated Inactive Tag"}
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_inactive_tag(self):
        url = reverse("tag-rud", args=[self.inactive_tag.slug])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
