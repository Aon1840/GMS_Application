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
import time
import datetime
import requests

# For Web Application
@csrf_exempt
def getAvailablePosition(request, floor_id):
    try:
        cursor = connection.cursor()
        cursor.execute("""select p.position_id, p.position_name,
        sum(p.is_available) as 'is_available',
        z.zone_name,
        f.floor_id,
        f.floor_name,
        b.building_id,
        b.building_name
        from Buildings_building b join Floors_floor f 
        on b.building_id = f.building_id
        join Zones_zone z
        on f.floor_id = z.floor_id
        join Positions_position p
        on z.zone_id = p.zone_id
        where f.floor_id = %s
        group by p.position_id
        order by p.position_id""", [floor_id])

    except:
        return HttpResponse("Hello from exception")

    items = []
    for row in cursor:
        items.append({
            'position_id': row[0],
            'position_name': row[1],
            'available_parking': int(row[2]),
            'zone_name': row[3],
            'floor_id': row[4],
            'floor_name': row[5],
            'building_id': row[6],
            'building_name': row[7],
        })

    context = {
        'position': items,
    }

    return render(request, 'Floors/floor_detail_10B.html', context)



# Service For Admin (Use Postman)
@csrf_exempt
def checkAvailablePosition(request, floor_id):
    try:
        cursor = connection.cursor()
        cursor.execute("""select p.position_id, p.position_name,
        sum(p.is_available) as 'is_available',
        z.zone_name,
        f.floor_id,
        f.floor_name,
        b.building_id,
        b.building_name
        from Buildings_building b join Floors_floor f 
        on b.building_id = f.building_id
        join Zones_zone z
        on f.floor_id = z.floor_id
        join Positions_position p
        on z.zone_id = p.zone_id
        where f.floor_id = %s
        group by p.position_id
        order by p.position_id""", [floor_id])

    except:
        return HttpResponse("Hello from exception")

    items = []
    for row in cursor:
        items.append({
            'position_id': row[0],
            'position_name': row[1],
            'available_parking': int(row[2]),
            'zone_name': row[3],
            'floor_id': row[4],
            'floor_name': row[5],
            'building_id': row[6],
            'building_name': row[7],
        })

    context = {
        'position': items,
    }

    return JsonResponse(context)


# For Mobile Application
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


@csrf_exempt
@api_view(['PUT'])
def carParking(request, position_id):
    position = _getPosition(position_id=position_id)
    if request.method == 'PUT':
        statusChange = request.data['is_available']
        position.is_available = statusChange
        position.save()
        t1 = datetime.datetime.now()
 
        serializer = PositionSerializer(position)
        t2 = datetime.datetime.now()

        # Save log in Parka Application Server
        _saveLogPosition(position_id=position_id, status=statusChange)
        t3 = datetime.datetime.now()

        print("--------", t1)
        print("--------", t2)
        print("--------", t3)

        return JsonResponse(serializer.data)

        
# Private Method
def _saveLogPosition(position_id, status):
    if position_id != None and status != None:
        path = 'http://localhost:8000/users/saveLog/%s/' % position_id
        status = status
        print("----- status: ",status)

        if status == "False":
            print("------ pass this line")
            position = requests.post(path, data={'isChangeTo':status})
        
        # requests.post('http://httpbin.org/post', data = {'key':'value'})

        return print("Save log position success!")


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