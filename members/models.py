from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=230, null=False, blank=False)
    message = models.TextField(max_length=2500, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-date"]
    def __str__(self):
        return f"{self.user} | {self.title} | {self.message} | {self.date}"