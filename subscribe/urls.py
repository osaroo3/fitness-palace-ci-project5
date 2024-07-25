from django.urls import path
from . import views
urlpatterns = [
    path('', views.view_subscription_plan, name='view_subcription_plan'),
]
