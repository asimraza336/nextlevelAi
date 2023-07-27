from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.conf import settings
from django.contrib.auth.hashers import make_password



class User(AbstractUser):
    # username = models.CharField(
    #     max_length=50, unique=True, primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, unique=True)
    avatar = models.FileField(upload_to="Avatar/", null=True, blank=True, default="Avatar/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.email)
    
    
class Avatar(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_avatar")
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    sale_area = models.CharField(max_length=130)
    territory = models.CharField(max_length=50)
    overview = models.CharField(max_length=400)
    website = models.CharField(max_length=70, null=True, blank=True)
    industry_type = models.CharField(max_length=60)
    specialities = models.CharField(max_length=60)
    company_size = models.IntegerField()
    headquaters = models.CharField(max_length=100, null=True, blank=True)
    
    
    
    
    
    
    
    
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
