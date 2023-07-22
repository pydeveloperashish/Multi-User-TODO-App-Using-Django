from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
    
# Create your views here.
def home(request):
    return render(request, 'index.html')


def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            print("Authenticated", user)
            if user:
                login(request, user)
                return redirect('home')
            
        else:
            context = {"form": form}
            return render(request, 'login.html', context)

    form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # print(form)
        context = { "form": form }
        if form.is_valid():
            user = form.save()
            print("user:", user)
            if user:
                return redirect('login')
        else:
            return render(request, 'signup.html', context = context)  
               
    form = UserCreationForm()    
    context = {
        "form": form,
    }
    return render(request, 'signup.html', context = context)