from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model"""

    def create_user(self, email, first_name, last_name, username, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have email address')
        if not username:
            raise ValueError('User must have username')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, username, password):
        """Creates a new super user with given details"""

        user = self.create_user(
            email, first_name, last_name, username, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a User Profile inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def get_first_name(self):
        """Use to get a users first name."""

        return self.first_name

    def get_last_name(self):
        """Use to get a users last name."""

        return self.last_name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.username


class TodoList(models.Model):
    """Users Todo list."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    todo_text = models.CharField(max_length=150)

    def __str__(self):
        """Return the model as the string."""

        return self.todo_text
