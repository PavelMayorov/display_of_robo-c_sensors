from django.urls import path

from . import views


app_name = 'display_sensors_app'
urlpatterns = [
    path('', views.index, name='index'),
]
