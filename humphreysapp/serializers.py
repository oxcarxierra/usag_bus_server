from rest_framework import serializers
from .models import *

class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = ('code', 'name', 'latitude','longitude')

class BusLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusLine
        fields = ('id', 'name')

class BusStopLineTableSerializer(serializers.ModelSerializer):
    bus_stop = BusStopSerializer()
    class Meta:
        model = BusStopLineTable
        fields = ('bus_stop', 'order')

class BusStopTimeTableSerializer(serializers.ModelSerializer):
    # bus_stop_line_table = BusStopLineTableSerializer()
    class Meta:
        model = BusStopTimeTable
        fields = ('arrival_time','weekend')