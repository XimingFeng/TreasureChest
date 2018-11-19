from django.urls import path

from . import views

urlpatterns = {
    path('', views.index, name="index"),
    path('register_computer', views.register_computer, name='register')
}