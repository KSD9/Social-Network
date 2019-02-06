from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Post
from .serializers import PostsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_post(title="", content=""):
        if title != "" and content != "":
            Post.objects.create(title=title, content=content)

    def set_up(self):
        # add test data
        self.create_post("Title 1", "sample content 1")
        self.create_post("Title 2", "sample content 2")


class GetAllPostsTest(BaseViewTest):

    def test_get_all_posts(self):
        """
        This test ensures that all posts added in the set up method
        exist when we make a GET request to the posts/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("posts-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Post.objects.all()
        serialized = PostsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)