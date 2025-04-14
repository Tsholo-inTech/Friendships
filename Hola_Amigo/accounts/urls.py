from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [

    path('', views.accounts_list, name = "lists"),
    path('profiles/', views.profiles_page, name="profilepage"), 
    path('new-account/', views.new_account, name="new_account"),
]