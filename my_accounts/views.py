from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
        if (username and password and password == password_check):
            new_user = User.objects.create_user(username=username, password=password)
            auth.login(request, new_user)
            return redirect('blog:home')

    return render(request, 'my_accounts/sign_up.html')

