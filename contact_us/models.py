from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    title = models.CharField(max_length=230)
    message = models.TextField(max_length=1500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
