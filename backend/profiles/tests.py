import random
import sys

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ProfileModelTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.users = [
            User.objects.create_user(f'tester{i}', f'tester{i}@gmail.com',
                                     f'testpasswd{i}') for i in range(5)
        ]
        cls.profiles = [u.profile for u in cls.users]

    def assertUserHasProfile(self, user):
        try:
            user.profile
        except User.profile.RelatedObjectDoesNotExist:
            self.fail('did not create a profile')

    def test_auto_create_on_user_create(self):
        """Test if a profile is created when a user is created."""
        # User = get_user_model()
        for i, user in enumerate(self.users):
            with self.subTest(i=i):
                self.assertUserHasProfile(user)

    def test_follow_unfollow(self):
        """Test if a profile is created when a user is created."""
        # User = get_user_model()
        a, b = random.sample(self.profiles, 2)
        a.follow(b)
        self.assertTrue(a.follows(b))
        a.unfollow(b)
        self.assertFalse(a.follows(b))
