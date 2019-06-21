from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Skill(models.Model):
    description = models.TextField(max_length=300)