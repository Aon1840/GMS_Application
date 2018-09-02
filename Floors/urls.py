from django.conf.urls  import url
from django.urls import path
from Floors import views

urlpatterns = [
    # For Web
    path('<building_id>', views.getAllFloorByBuildingId, name='getAllFloor'),

    # Service For Admin


    # For Mobile
    path('getAllFloor/<building_id>', views.getFloors, name='getFloors'),
]