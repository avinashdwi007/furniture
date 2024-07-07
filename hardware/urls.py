
from django.urls import include, path

from hardware import views

urlpatterns = [
    path('', views.index,name='home'),
]
