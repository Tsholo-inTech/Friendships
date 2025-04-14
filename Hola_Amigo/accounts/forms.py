from django import forms
from .import models

class CreateAccount(forms.ModelForm):
    
    class Meta:
        model = models.Profile
        fields = ['firstname','lastname', 'username', 'bio', 'profile_image','social_linkedin']
