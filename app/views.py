from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
    
# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


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