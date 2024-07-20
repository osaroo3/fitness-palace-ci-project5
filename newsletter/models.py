from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Newsletter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.user} | {self.email} Subscribed"