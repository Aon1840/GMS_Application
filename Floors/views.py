from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from Floors.models import Floor
from Adapter.serializers import FloorSerializer
from django.db import connection
import json

# For Web Application
@csrf_exempt
def getAllFloorByBuildingId(request, building_id):
    try:
        floors = _getAllFloors(building_id=building_id)

        if floors.count() > 0:
            message = None
        else:
            floors = None
            message = "Does not have a Floor now"
    except:
        floors = None
        message = "Does not Exits"

    if request.method == 'GET':
        context = {
            'floors': floors,
            'message': message
        }

        return render(request, 'Floors/floor_list.html', context)


# @csrf_exempt
# def getAvailableAllFloor(request, building_id):
#     cursor = connection.cursor()
#     cursor.execute("""
    
#     """)


# Service For Admin (Use Postman)


# For Mobile Application
@csrf_exempt
def getFloors(request, building_id):
    try:
        floors = _getAllFloors(building_id=building_id)

        if floors.count() > 0:
            message = None
        else:
            floors = None
            message = "Do not have a Floor now."
    except Exception as e:
        message = "Does not Exits."

    if request.method == 'GET':
        serializer = FloorSerializer(floors, many=True)
        context = {
            'floors': serializer.data,
            'message': message
        }

        return JsonResponse(context)

# Private Method
def _getFloor(floor_id):
    if floor_id != None:
        try:
            floor = Floor.objects.get(floor_id=floor_id)
        except Exception as e:
            return HttpResponse(e)

        return floor


def _getAllFloors(building_id):
    if building_id != None:
        try:
            floors = Floor.objects.filter(building_id=building_id).order_by('floor_id')
        except Exception as e:
            return HttpResponse(e)

        return floors
