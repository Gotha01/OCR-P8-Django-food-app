from django.test import TestCase
from authentication.models import MyUser, MyUserManager

class MyUserManagerTestCase(TestCase):
    def setUp(self):
        self.user_manager = MyUserManager()

    def test_create_user_no_email(self):
        """Test creating a user without an email"""
        with self.assertRaises(ValueError):
            self.user_manager.create_user(email='', username='testuser')

    def test_create_user_no_username(self):
        """Test creating a user without a username"""
        with self.assertRaises(ValueError):
            self.user_manager.create_user(email='testuser@test.com', username='')
    
    def test_create_user(self):
        email = "test@example.com"
        username = "testuser"
        password = "testpassword"

        # Crée un nouvel utilisateur
        user = MyUser.objects.create_user(email=email, username=username, password=password)

        # Vérifie si les attributs sont corrects
        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        email = "test@example.com"
        username = "testuser"
        password = "testpassword"

        # Crée un nouveau super-utilisateur
        superuser = MyUser.objects.create_superuser(email=email, username=username, password=password)

        # Vérifie si les attributs sont corrects
        self.assertEqual(superuser.email, email)
        self.assertEqual(superuser.username, username)
        self.assertTrue(superuser.check_password(password))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)