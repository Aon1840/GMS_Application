from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from Positions.models import Position
from Zones.models import Zone
from Floors.models import Floor
from Buildings.models import Building
from Adapter.serializers import PositionSerializer
from django.db import connection
import json

# For Web Application



# Service For Admin (Use Postman)



# For Mobile Application
# def getPositionsByFloor(request, floor_id):
#     try:
#         positions = _getAllPositionByFloor(floor_id=floor_id)

#         if positions.count() > 0:
#             message = None
#         else:
#             message = "Do not have a Position now."
#     except Exception as e:
#         message = "Does not Exits." 

#     if request.method == 'GET':
#         serializer = PositionSerializer(positions, many=True)
#         context = {
#             'zones': serializer.data,
#             'message': message
#         }

#     return JsonResponse(context)

def getPositionDetail(request, position_id):
    try:
        position = _getPosition(position_id=position_id)
        zone_id = position.zone_id
    except Exception as e:
        return HttpResponse(e)

    if request.method == 'GET':
        zone = Zone.objects.get(zone_id=zone_id)
        floor_id = zone.floor_id

        floor = Floor.objects.get(floor_id=floor_id)
        building_id = floor.building_id

        building = Building.objects.get(building_id=building_id)

        context = {
            'position_id': position_id,
            'position_name': position.position_name,
            'status': position.is_available,
            'zone_name': zone.zone_name,
            'floor_name': floor.floor_name,
            'building_name': building.building_name
        }

        return JsonResponse(context) 



def getPositionsByFloor(request, floor_id):
    try:
        positions = _getAllPositionByFloor(floor_id=floor_id)

    except Exception as e:
        HttpResponse(e)

    if request.method == 'GET':
        serializer = PositionSerializer(positions, many=True)

    return JsonResponse(serializer.data, safe=False)


# Private Method
def _getPosition(position_id):
    if position_id != None:
        try:
            position = Position.objects.get(position_id=position_id)
        except Exception as e:
            return HttpResponse(e)

        return position


def _getAllPositionByFloor(floor_id):
    if floor_id != None:
        try:
            positions = Position.objects.filter(zone_id__floor_id=floor_id)
        except Exception as e:
            return HttpResponse(e)

        return positions


def _getAllPositionByZone(zone_id):
    if zone_id != None:
        try:
            positions = Position.objects.filter(zone_id=zone_id)
        except Exception as e:
            return HttpResponse(e)

        return positions