from distutils.command.build_scripts import build_scripts
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from humphreysapp.models import *
from .serializers import *
# Create your views here.

@csrf_exempt
def bus_stop_list(request):
    if request.method == 'GET':
        queryset = BusStop.objects.all()
        serializer = BusStopSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def bus_line_list(request):
    if request.method == 'GET':
        queryset = BusLine.objects.all().order_by('id')
        serializer = BusLineSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def bus_line_detail(request, line):
    if request.method == 'GET':
        bus_line = BusLine.objects.get(name=line)
        queryset = BusStopLineTable.objects.filter(bus_line=bus_line).order_by('order')
        serializer = BusStopLineTableSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def bus_stop_detail(request, stop_id, weekend):
    result=[]
    if request.method == 'GET':
        weekend_boolean = True if weekend=='True' else False
        bus_stop = BusStop.objects.get(code=stop_id)
        line_list = BusStopLineTable.objects.filter(bus_stop=bus_stop)
        for line in line_list:
            queryset = BusStopTimeTable.objects.filter(bus_stop_line_table=line, weekend=weekend_boolean).values('arrival_time')
            serializer = BusStopTimeTableSerializer(queryset, many=True)
            arrival_time = []
            for time in serializer.data:
                arrival_time.append(time['arrival_time'])
            next_stop = BusStopLineTable.objects.get(bus_line=line.bus_line, order=(1 if line.order==line.bus_line.length else line.order+1))
            result.append({'line':line.bus_line.name,'order':line.order,'next_stop':next_stop.bus_stop.name, 'arrival_time':arrival_time})
        return JsonResponse(result, safe=False)