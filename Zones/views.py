from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from Zones.models import Zone
from Adapter.serializers import ZoneSerializer
from django.db import connection
import json

# For Web Application



# Service For Admin (Use Postman)



# For Mobile Application
def getZones(request, floor_id):
    try:
        zone = _getAllZone(floor_id=floor_id)

        if zone.count() > 0:
            message = None
        else:
            zone = None
            message = "Do not have a Zone now."
    except Exception as e:
        message = "Does not Exits." 

    if request.method == 'GET':
        serializer = ZoneSerializer(zone, many=True)
        context = {
            'zones': serializer.data,
            'message': message
        }

    return JsonResponse(context)


# Private Method
def _getZone(zone_id):
    if zone_id != None:
        try:
            zone = Zone.objects.get(zone_id=zone_id)
        except Exception as e:
            return HttpResponse(e)
        
        return zone


def _getAllZone(floor_id):
    if floor_id != None:
        try:
            zones = Zone.objects.filter(floor_id=floor_id)
        except Exception as e:
            return HttpResponse(e)

        return zones


def _getZoneByBuilding(building_id):
    if building_id != None:
        try:
            zones = Zone.objects.filter(floor_id__building_id=building_id)
        except Exception as e:
            return HttpResponse(e)
        
        return zones