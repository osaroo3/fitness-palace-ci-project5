from django.contrib import admin
from .models import Newsletter
# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):
    """ View info from newsletter form in backend """
    list_display = (
        'user',
        'email',
    )


admin.site.register(Newsletter)
