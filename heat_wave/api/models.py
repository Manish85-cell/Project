from django.db import models
import random
import string
def generates_unique_password():
     length = 8
     
     while True:
         password = ''.join(random.choices(string.ascii_uppercase, k = length))    
         if User.objects.filter(password=password).count() == 0:
              break
     return password

def generate_unique_username():
    length = 8
    
    while True:
        username = ''.join(random.choices(string.ascii_lowercase, k = length))
        if User.objects.filter(username=username).count() == 0:
            break
    return username
          
# Create your models here.
class User(models.Model):
    email_id  = models.CharField(max_length=64,default="", unique=True)
    username = models.CharField(max_length = 16 , default = generate_unique_username, unique=True, primary_key=True)
    password = models.CharField(max_length=16, default=generates_unique_password)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Problem(models.Model):
    
    difficulty_level = [
        ('E','Easy'),
        ('M','Medium'),
        ('D','Difficult'),
        ('T','Tricky'),
    ]
     
    Problem_id  = models.CharField(max_length=64,default=generates_unique_password, unique=True)
    statement = models.CharField(max_length = 16 , default = "", unique=True)
    level = models.CharField(max_length=16,  choices=difficulty_level, default="E")
    solution = models.CharField(max_length=2048, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    
    