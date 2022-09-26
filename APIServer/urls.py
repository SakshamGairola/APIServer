from django.urls import path

from . import views

urlpatterns = [
    path('api', views.apiendpoint, name='apiendpoint'),
    path('api/<int:id>', views.apiendpointid, name='apiendpointid'),
]
