from django.conf.urls  import url
from django.urls import path
from Positions import views

urlpatterns = [
    # For Web
    

    # Service For Admin


    # For Mobile
    path('getAllPositionByFloor/<floor_id>', views.getPositionsByFloor, name='getPositionsByFloor'),
    path('<position_id>/getPositionDetail', views.getPositionDetail, name='getPositionDetail'),
]