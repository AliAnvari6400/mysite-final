from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

User._meta.get_field('email')._unique = True
