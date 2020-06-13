from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Login_table(models.Model):
    
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=129)
    def __str__(self):
        return self.user
