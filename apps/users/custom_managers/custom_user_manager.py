from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Enter Valid Email')
        email=self.normalize_email(email)      
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        

        return user
    
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff')is not True:
            raise ValueError("User must be is_staff")
        if extra_fields.get('is_superuser')is not True:
            raise ValueError("User must be is_superuser")
        return self.create_user(email, password, **extra_fields)


