from django.db import models
from django.contrib.auth.models import AbstractUser;

# Create your models here.
class User(AbstractUser):
      image = models.ImageField(upload_to='users_images', null=True, blank=True)
      
      class Meta:
            db_table = 'user'
            verbose_name = 'Пользователь'
            verbose_name_plural = 'Пользователи'
            
      def __str__(self):
            return self.username
            