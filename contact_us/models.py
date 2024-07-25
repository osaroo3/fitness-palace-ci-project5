from django.db import models

# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    title = models.CharField(max_length=230, null=False, blank=False)
    message = models.TextField(max_length=2500, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
