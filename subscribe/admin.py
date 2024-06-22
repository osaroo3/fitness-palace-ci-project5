from django.contrib import admin
from .models import Plan, Category
# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'description',
        'duration',
    )

    ordering = ('price',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Plan, PlanAdmin)
admin.site.register(Category, CategoryAdmin)