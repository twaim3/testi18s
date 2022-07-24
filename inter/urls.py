from django.urls import path
from . import views

app_name='inter'
urlpatterns = [
    path('', views.home, name='home'),
]
