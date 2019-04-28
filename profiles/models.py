from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
	"""Helps django to work with our custom user model"""
		
	def create_user(self, email, name, password=None):
		"""Creates a new user profile."""

		if not email:
			raise ValidationError("User must have an email.")

		email = self.normalize_email(email)
		user = self.model(email=email, name=name)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		"""Creates and saves a new superuser with given details."""

		user = self.create_user(email, name, password)

		user.is_superuser = True
		user.save(using=self._db)

		return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Represents UserProfile"""
	
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

	objects = UserProfileManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		"""Used to get full name of the user"""
		
		return self.name
		
	def get_short_name(self):
		"""Used to get full name of the user"""

		return self.name

	def __str__(self):
		"""Used to convert the object to string"""

		return self.email
