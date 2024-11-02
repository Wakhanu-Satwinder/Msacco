import pytest
import unittest
from django.contrib.auth import get_user_model
from django.test import TestCase
from sacco.models import CustomUser


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = CustomUser.objects.create_user(email="baller@gmail.com", password="1234")
        self.assertEqual(user.email, "baller@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            CustomUser.objects.create_user()
        with self.assertRaises(TypeError):
            CustomUser.objects.create_user(email="")
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False)



@pytest.mark.django_db
def test_user_create():
  CustomUser.objects.create_user(email='st@gmail.com',password='satpassword')
  assert CustomUser.objects.count() == 1       