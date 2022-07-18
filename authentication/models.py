from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):
    """User manager class"""

    def create_user(self, email, username, password=None):
        """Function to create a new user.

        Args:
            email (str): Email to be filled in for the creation of a new user.
            username (str): Username to be filled in for the creation of a new user.
            password (str, optional): Password to be filled in for the creation of a new user. Defaults to None.

        Raises:
            ValueError: raised when the email field is not filled in.
            ValueError: raised when the username field is not filled in.

        Returns:
            user: A new user is added to the database.
        """
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")

        user=self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None):
        """Function to create a new superuser.

        Args:
            email (str): Email to be filled in for the creation of a new.
            username (str): Username to be filled in for the creation of a new.
            password (str, optional): Email to be filled in for the creation of a new. Defaults to None.

        Returns:
            user: A new superuser is added to the database.
        """
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    """Customized user class."""
    email = models.EmailField('email', max_length=60, unique=True)
    username = models.CharField('username', max_length=50)
    user_img = models.ImageField(null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['username']

    objects=MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True