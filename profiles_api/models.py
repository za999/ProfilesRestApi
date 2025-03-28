from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for UserProfile"""

    def create_user(self, email, name, password=None):
        """Creates a new user profile"""
        if not email:
            raise ValueError('User must have an email!')

        # Normalize the email means making the second half lowercase.
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # Using the AbstractBaseUser set password function. Will has the pwd.
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and save a new super/user with details"""
        user = self.create_user(email, name, password)

        # is_superuser is automatically created in PermissionsMixin
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get full name of user"""
        return self.name

    def get_short_name(self):
        """Get short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE # This tells the db to cascade the items incase the associated UserProfile is deleted.
    )
    status_text = models.CharField(max_length=255) # Contains the text of the feed item update
    created_on = models.DateTimeField(auto_now_add=True) # Every time an item is created, sets the time it was created

    def __str__(self):
        """Return the item model as a string"""
        return self.status_text
