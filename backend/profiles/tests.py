import random
import sys

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from profiles.models import Profile

UserModel = get_user_model()


class ProfileModelTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        for i in range(5):
            User.objects.create_user(
                username=f'tester{i}',
                email=f'tester{i}@gmail.com',
                password=f'testpasswd{i}',
            )

    def assertUserHasProfile(self, user):
        try:
            user.profile
        except User.profile.RelatedObjectDoesNotExist:
            self.fail('did not create a profile')

    def test_auto_create_on_user_create(self):
        """Test if a profile is created when a user is created."""
        for i, user in enumerate(UserModel.objects.all()):
            with self.subTest(i=i):
                self.assertUserHasProfile(user)

    def get_2_random_profiles(self):
        while True:
            a, b = random.choices(Profile.objects.all(), k=2)
            if a != b:
                break
        return a, b

    def test_follow_unfollow(self):
        """Test if a profile is created when a user is created."""
        a, b = self.get_2_random_profiles()

        a.follow(b)
        self.assertTrue(a.follows(b))
        a.unfollow(b)
        self.assertFalse(a.follows(b))
