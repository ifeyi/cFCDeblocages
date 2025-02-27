from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .utils import deblocage_authenticate

def home(request):

    if request.method == 'POST':
        deblocage_usermail = request.POST['deblocage-usermail']
        deblocage_password = request.POST['deblocage-password']

        user = deblocage_authenticate(email=deblocage_usermail, password=deblocage_password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Vous êtes connecté')
            return redirect('home')
        else:
            messages.error(request, 'Identifiants incorrects!')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    pass