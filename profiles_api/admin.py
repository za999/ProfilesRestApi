from django.contrib import admin
from profiles_api import models

# Registers the UserProfile model to Django Admin interface
admin.site.register(models.UserProfile)
