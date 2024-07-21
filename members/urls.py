from django.urls import path
from . import views
urlpatterns = [
    path('', views.members_info, name='members_info'),
]