from django.urls import path, re_path

from . import views

app_name = "shopping"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('shopping/', views.shopping, name='shopping'),

]
