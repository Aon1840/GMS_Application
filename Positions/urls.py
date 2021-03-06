from django.conf.urls  import url
from django.urls import path
from Positions import views

urlpatterns = [
    # For Web
    path('getAvailablePosition/<floor_id>', views.getAvailablePosition, name='getAvailablePosition'),

    # Service For Admin
    path('checkAvailablePosition/<floor_id>', views.checkAvailablePosition, name='checkAvailablePosition'),

    # For Mobile
    path('getAllPositionByFloor/<floor_id>', views.getPositionsByFloor, name='getPositionsByFloor'),
    path('<position_id>/getPositionDetail', views.getPositionDetail, name='getPositionDetail'),
    path('<position_id>/parking', views.carParking, name='carParking'),
    path('<position_id>/driveout', views.carDriveOut, name='carDriveOut'),
]