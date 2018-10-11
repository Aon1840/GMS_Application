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

# ---------------------------------- For Web Application ----------------------------------
@csrf_exempt
def getAllBuilding(request):
    try:
        buildings = _getBuilding()

        if buildings.count() > 0:
            message = None
        else:
            buildings = None
            message = "Do not have a building now."
    except:
        buildings = None
        message = "Does not Exits"

    context = {
        'buildings': buildings,
        'message': message
    }
    return render(request, 'Buildings/building_list.html', context)


@csrf_exempt
def getAvailableAllBuilding(request):
    try:
        cursor = connection.cursor()
        cursor.execute("""SELECT b.building_id,
        b.building_name,
        SUM(1-p.is_available) as 'use',
        SUM(p.is_available) as 'available_parking',
        COUNT(*) as 'total_parking'
        FROM Buildings_building b JOIN Floors_floor f
        ON b.building_id = f.building_id
        JOIN Zones_zone z
        ON f.floor_id = z.floor_id
        JOIN Positions_position p
        ON z.zone_id = p.zone_id
        GROUP BY b.building_name
        ORDER BY b.building_id""")
        
        if cursor.count() > 0:
            message = None
        else:
            items = None
            message = "Do not have a building now."

    except:
        items = None
        message = "Does not Exits"

    items = []
    for row in cursor:
        items.append({
            'building_id': row[0],
            'building_name': row[1],
            'use': row[2],
            'available_parking': row[3],
            'total_parking': row[4],
        })

    context = {
        'buildings': items,
        'message': message
    }
    return render(request, 'Buildings/building_list.html', context)


# ---------------------------------- Service For Admin (Use Postman) ----------------------------------
@csrf_exempt
def addNewBuilding(request):
    if request.method == 'POST':
        serializer = BuildingSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)


@csrf_exempt
@api_view(['PUT'])
def editBuildingNameById(request, building_id):
    try:
        building = _getBuilding(building_id=building_id)
    except Exception as e:
        return HttpResponse(e)

    if request.method == 'PUT':
        serializer = BuildingSerializer(building, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)


@csrf_exempt
@api_view(['DELETE'])
def deleteBuildingById(request, building_id):
    try:
        building = _getBuilding(building_id=building_id)
    except Exception as e:
        return HttpResponse(e)

    if request.method == 'DELETE':
        building.delete()
        return HttpResponse("Delete Success")


# ---------------------------------- For Mobile Application ----------------------------------
@csrf_exempt
def getBuildings(request):
    try:
        buildings = _getAllBuilding()
        message = None
        if buildings.count() > 0:
            message = None
        else:
            message = "Do not have a building now"
    except:
        message = "Does not Exits"

    if request.method == 'GET':
        serializer = BuildingSerializer(buildings, many=True)
        context = {
            'results': serializer.data,
            'message': message
        }
        return JsonResponse(context)


# ---------------------------------- Private Method ----------------------------------
# def _getBuilding(building_id):
#     if(building_id != None):
#         try:
#             buildings = Building.objects.get(building_id=building_id)
#         except Exception as e:
#             return HttpResponse(e)

#     return buildings


def _getAllBuilding():
    try:
        buildings = Building.objects.all()
    except Exception as e:
        return HttpResponse(e)

    return buildings

def _getBuilding(building_id):
    if building_id != None:
        building = Building.objects.get(building_id=building_id)
    else:
        building = Building.objects.all()

    return building

