from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse

# class-based views
"""
    ListView = get a list of records
    DetailView = get the details of a record
    CrateView = create a new record
    DeleteView = delete record
    UpdateView = update record
    LoginView = login 
"""

# Create your views here.
class UserLoginView(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        # after login, send the user to:
        return reverse('home')