from django.urls import path
from .views import home, loginUser, signup, add_todo, logoutUser, delete_todo, change_todo

urlpatterns = [
    path('', view = home, name = 'home'),
    path('login/', view = loginUser, name = 'login'),
    path('signup/', view = signup, name = 'signup'),
    path('logout/', view = logoutUser, name = 'logout'),
    path('add-todo/', view = add_todo, name = 'add_todo'),
    path('delete-todo/<int:id>/', view = delete_todo, name = 'delete_todo'),
    path('change-todo/<int:id>/<str:status>', view = change_todo, name = 'change-todo'),    
]
