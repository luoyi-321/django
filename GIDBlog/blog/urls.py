from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index),
    path('edit',views.edit),
    path('me',views.me),
    
]
