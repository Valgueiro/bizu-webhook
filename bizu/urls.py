from django.urls import path

from . import views

urlpatterns = [
    path('hooks', views.process, name='hooks'),
]
