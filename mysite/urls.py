from django.urls import path,include
from mysite import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('form',views.form),
    path('<int:person_id>',views.person,name='person'),
]
