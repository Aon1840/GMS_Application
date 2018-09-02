from django.conf.urls  import url
from django.urls import path
from Zones import views

urlpatterns = [
    # For Web
    

    # Service For Admin


    # For Mobile
    path('getAllZone/<floor_id>', views.getZones, name='getZones')
]