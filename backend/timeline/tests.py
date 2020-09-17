import os.path
import random
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.images import ImageFile
from rest_framework.test import APITestCase

from timeline.models import Post

UserModel = get_user_model()

TEST_IMAGE_PATH = Path(os.path.dirname(__file__), 'test_image.jpg')


class PostModelTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            UserModel.objects.create_user(
                username=f'tester{i}',
                password=f'testpass{i}',
            )
        cls.test_image = ImageFile(open(TEST_IMAGE_PATH, 'rb'))
        for u in UserModel.objects.all():
            Post.objects.create(
                user=u,
                description=f'{u.username}´s post',
                image=cls.test_image,
            )

    @classmethod
    def tearDownClass(cls):
        Post.objects.all().delete()
        super().tearDownClass()

    def test_image_delete_on_model_delete(self):
        post = random.choice(Post.objects.all())
        image_path = Path(settings.MEDIA_ROOT, post.image.name)
        self.assertTrue(
            image_path.exists(),
            f'la imagen no se guardó corectamente: {image_path}',
        )
        post.delete()
        self.assertFalse(
            image_path.exists(),
            f'la imagen no se eliminó correctamente: {image_path}',
        )
