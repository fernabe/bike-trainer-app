from django.urls import path

from . import views

app_name = 'trainer'

urlpatterns = [
    # ex: /trainer/
    path('', views.index, name='index'),
]