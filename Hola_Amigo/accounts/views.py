from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def accounts_list(request):
    accounts = Profile.objects.all().order_by('-created')
    return render(request, 'accounts/accounts_list.html', {'accounts': accounts})

def profiles_page(request):
    profilepage = get_object_or_404(Profile, username = request.user.username) 
    return render(request, 'accounts/profile_page.html', {'profilepage': profilepage})    



@login_required(login_url = "/users/login/")

def new_account(request):
    if request.method == 'POST': 
        form = forms.CreatePost(request.POST, request.FILES) 
        if form.is_valid():
            newaccount = form.save(commit=False)
            #newaccount.username = request.user 
            newaccount.save()
            return redirect('posts:lists')        
    else:
        form = forms.CreateAccount()
    return render(request, 'accounts/new_account.html', {'form': form})
 