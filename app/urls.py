from django.urls import path
from .views import home, loginUser, signup, add_todo, logoutUser

urlpatterns = [
    path('', view = home, name = 'home'),
    path('login/', view = loginUser, name = 'login'),
    path('signup/', view = signup, name = 'signup'),
    path('logout/', view = logoutUser, name = 'logout'),
    path('add-todo/', view = add_todo, name = 'add_todo'),
    
]
