from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass




# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission

# import random
# import string

# def generates_unique_password():
#      length = 8
     
#      while True:
#          password = ''.join(random.choices(string.ascii_uppercase, k = length))    
#          if User.objects.filter(password=password).count() == 0:
#               break
#      return password

# def generate_unique_username():
#     length = 8
    
#     while True:
#         username = ''.join(random.choices(string.ascii_lowercase, k = length))
#         if User.objects.filter(username=username).count() == 0:
#             break
#     return username

# # Create your models here.
# class User(AbstractUser):
#     email_id  = models.CharField(max_length=64,default="", unique=True)
#     username = models.CharField(max_length = 16 , default = generate_unique_username, unique=True, primary_key=True)
#     password = models.CharField(max_length=16, default=generates_unique_password)
#     created_at = models.DateTimeField(auto_now_add=True)
#     groups = models.ManyToManyField(
#         Group,
#         related_name='oj_user_set',  # Use a different related name
#         blank=True,
#         help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
#         related_query_name='user',
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='oj_user_set',  # Use a different related name
#         blank=True,
#         help_text=('Specific permissions for this user.'),
#         related_query_name='user',
#     )