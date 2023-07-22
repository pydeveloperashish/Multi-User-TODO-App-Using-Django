from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
# Create your models here.
class Todo(models.Model):
    status_choices = [
        ('C','COMPLETED'),
        ('P', 'PENDING'),
    ]  
    priority_choices = [
        ('1','1️⃣'),
        ('2', '2️⃣'),
        ('3','3️⃣'),
        ('4', '4️⃣'),
        ('5','5️⃣'),
        ('6', '6️⃣'), 
        ('7','7️⃣'),
        ('8', '8️⃣'),
        ('9','9️⃣'),
        ('10', '🔟'),
    ]
    
    title = models.CharField(max_length = 50)
    status = models.CharField(max_length = 2, choices = status_choices, default = "")
    # user is ForeignKey:- if user is deleted, his/her todo will be deleted.
    user = models.ForeignKey(User, on_delete = models.CASCADE,  default = "")
    date = models.DateTimeField(auto_now_add = True) # current date and time.
    priority = models.CharField(max_length = 2, choices = priority_choices, default = "")
    