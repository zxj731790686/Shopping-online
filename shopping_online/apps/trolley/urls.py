from django.urls import path, re_path

from . import views

app_name = "trolley"

urlpatterns = [
    path('trolley/', views.trolley, name='trolley'),

]