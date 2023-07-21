from django.urls import path
from django.http import HttpResponse

def home(request):
    print("hello world..this is home")
    return HttpResponse("<h1>Hello World</h1>")

urlpatterns = [
    path('', view = home)
]
