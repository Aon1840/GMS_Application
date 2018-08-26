from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from Buildings.models import Building
from Adapter.serializers import BuildingSerializer
from django.db import connection
import json

@csrf_exempt
def getAllBuilding(request):
    try:
        buildings = Building.objects.all()
        message = None
    except:
        message = "Do not have a building now."
        # return HttpResponse("false")

    if request.method == 'GET':
        # serializer = BuildingSerializer(buildings, many=True)
        context = {
            'buildings': buildings,
            'message': message
        }
    return render(request, 'Buildings/building_list.html', context)


# For Mobile Application
@csrf_exempt
def getBuildings(request):
    try:
        buildings = Building.objects.all()
        message = None
    except:
        message = "Do not have a building now."

    if request.method == 'GET':
        serializer = BuildingSerializer(buildings, many=True)
        context = {
            'results': serializer.data,
            'message': message
        }
        return JsonResponse(context)
