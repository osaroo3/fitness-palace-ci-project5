from django.contrib import admin
from .models import Membership
# Register your models here.


class MembershipAdmin(admin.ModelAdmin):
    """ View info from members form in backend """
    list_display = (
        'user',
        'title',
        'message',
        'date',
    )


admin.site.register(Membership)
