from django.db import models
#from django.contrib.auth.models import AbstractUser

# Create your models here.


class Profile(models.Model):
    #user = models.OneToOneField(StudentAccount, on_delete=models.CASCADE, related_name='profile')
    firstname = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=200, blank=True, null=True)
    studentnum = models.CharField(max_length=20, blank=True)
    school_email = models.EmailField(max_length=10, blank=True, null=True )
    username = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(null=True, blank=True, default="default-user.webp")
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['firstname','lastname','student_number','school_email','username']
    

    def __str__(self):
        return self.username or "Unnamed Profile"