from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('<p_id>', views.view_sub_checkout, name='view_sub_checkout'),
    path('plans/', views.view_my_plan, name='view_my_plan'), 
    path('cache_sub_checkout_data/', views.cache_sub_checkout_data, name='cache_sub_checkout_data'),
    path('wh/', webhook, name='webhook'),
]