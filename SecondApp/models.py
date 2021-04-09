from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=40)
    
    def __str__(self):
        return self.username

#class Signup(models.Model):
#    first_name=models.CharField(max_length=30)
#    last_name=models.CharField(max_length=30)
#    password=models.CharField(max_length=40)
#    verify_password=models.CharField(max_length=40)
        
#    def __str__(self):
#        return self.first_name

#class Loginn(models.Model):
#    username=models.CharField(max_length=30)
#    email=models.EmailField(max_length=30)
#    password=models.CharField(max_length=40)
    
#    def __str__(self):
#        return self.username