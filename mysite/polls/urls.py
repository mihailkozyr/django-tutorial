from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('hello/', views.hello, name='hello'),
   path('preved/', views.medved, name='hello'),
]