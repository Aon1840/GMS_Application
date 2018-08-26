from django.conf.urls  import url
from django.urls import path
from Buildings import views

urlpatterns = [
    # For Web
    path('', views.getAllBuilding, name='getAllBuilding'),


    # For Mobile
    path('getBuildings', views.getBuildings, name='getBuildings')
]