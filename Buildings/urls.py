from django.conf.urls  import url
from django.urls import path
from Buildings import views

urlpatterns = [
    # For Web
    # path('', views.getAllBuilding, name='getAllBuilding'),
    path('', views.getAvailableAllBuilding, name='getAllBuilding'),

    # Service For Admin
    path('addNewBuilding', views.addNewBuilding, name='addNewBuilding'),
    path('editBuilding/<building_id>', views.editBuildingNameById, name='editBuilding'),
    path('deleteBuilding/<building_id>', views.deleteBuildingById, name='deleteBuilding'),

    # For Mobile
    path('getBuildings', views.getBuildings, name='getBuildings')
]