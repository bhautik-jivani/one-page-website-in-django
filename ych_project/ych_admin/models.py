from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from passlib.hash import pbkdf2_sha256

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=20, null=False)
    user_email = models.CharField( max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], unique=True)
    user_pass = models.CharField(max_length=25)

    def __str__(self):
        return self.user_name

class Home(models.Model):
    home_title = models.CharField(max_length=250, null=False)
    home_content = models.TextField()

    def __str__(self):
        return self.home_title

class HomeButton(models.Model):
    home_btn = models.CharField(max_length=20, null=False)
    home_btn_class = models.CharField(max_length=50, default='btn btn-primary')
    home_btn_link = models.CharField(max_length=300, default='#')

    def __str__(self):
        return self.home_btn

class Menu(models.Model):
    menu = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.menu

class Service(models.Model):
    service_title = models.CharField(max_length=250, null=False)
    service_i_tag = models.CharField(max_length=50, default='fas fa-cog')
    service_content = models.TextField(null=False)
    

    def __str__(self):
        return self.service_title

class Gallery(models.Model):
    img = models.ImageField(upload_to='gallery/',max_length=100)

class About(models.Model):
    about_content = models.TextField()

    def __str__(self):
        return self.about_content

class Contact(models.Model):
    contact_num = models.CharField( max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], unique=True)
    contact_title = models.CharField(max_length=100)
    contact_address = models.TextField()
    

    def __str__(self):
        return self.contact_num
