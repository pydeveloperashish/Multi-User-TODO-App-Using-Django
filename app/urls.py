from django.urls import path
from .views import home, loginUser, signup

urlpatterns = [
    path('', view = home, name = 'home'),
    path('login/', view = loginUser, name = 'login'),
    path('signup/', view = signup, name = 'signup'),
]
