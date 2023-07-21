from django.urls import path
from .views import home, login, signup

urlpatterns = [
    path('', view = home, name = 'home'),
    path('login/', view = login, name = 'login'),
    path('signup/', view = signup, name = 'signup'),
]
