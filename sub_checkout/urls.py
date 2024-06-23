from django.urls import path
from . import views
urlpatterns = [
    path('<p_id>', views.view_sub_checkout, name='view_sub_checkout'), 
]