from django.urls import path

from . import views

app_name = "programmer"

urlpatterns = [
    path('', views.home, name='home'),
]