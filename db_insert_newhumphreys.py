import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'bus_app_api.settings.dev') 
# python이 실행될 때 DJANGO_SETTINGS_MODULE라는 환경 변수에
# 현재 프로젝트의 settings.py 파일 경로를 등록
django.setup() # python manage.py shell 을 실행하는 것이랑 비슷한 방법이다. 즉 파이썬 파일에서도 django를 실행 시킬수 있다.

# import model
from newhumphreysapp.models import *

# Menu Table 
def insert_bus_line():
  if BusLine.objects.exists():
    print('DATA EXISTS!')     
  else:
    with open('data/new_humphreys/bus_line_data.csv', newline='', encoding='utf8') as csvfile:
        data_reader = csv.reader(csvfile)
        for row in data_reader:
            BusLine.objects.create(
                name =row[0],
                length = row[1],
                )
    print('DATA UPLOADED SUCCESSFULY!')    

def insert_bus_stop():
  if BusStop.objects.exists():
    print('DATA EXISTS!')   
  else:
    with open('data/new_humphreys/bus_stop_data.csv', newline='', encoding='utf8') as csvfile:
      data_reader = csv.reader(csvfile)
      for row in data_reader:
          BusStop.objects.create(
              code =row[0],
              name =row[1],
              latitude = row[2],
              longitude = row[3]
              )
      print('DATA UPLOADED SUCCESSFULY!')   

def insert_bus_stop_line():    
  if BusStopLineTable.objects.exists():
    print('DATA EXISTS!')   
  else:
    with open('data/new_humphreys/bus_stop_line_data.csv', newline='', encoding='utf8') as csvfile:
        data_reader = csv.reader(csvfile)
        for row in data_reader:
            bus_line = BusLine.objects.get(id=row[0])
            bus_stop = BusStop.objects.get(code=row[1])
            order = row[2]
            BusStopLineTable.objects.create(
                bus_line = bus_line,
                bus_stop = bus_stop,
                order = order
                )
        print('DATA UPLOADED SUCCESSFULY!')    

def insert_bus_stop_time():    
  if BusStopTimeTable.objects.exists():
    print('DATA EXISTS!')   
  else:
    for day in ['reg','fri','sat','sun']:
      with open(f'data/new_humphreys/bus_stop_time_{day}.csv', newline='', encoding='utf8') as csvfile:
          data_reader = csv.reader(csvfile)
          for row in data_reader:
              bus_stop_line_table = BusStopLineTable.objects.get(bus_line=row[0],bus_stop=row[1],order=row[2])
              for i in range(3,len(row)-1):
                  BusStopTimeTable.objects.create(
                  bus_stop_line_table = bus_stop_line_table,
                  day=day,
                  arrival_time=row[i])
      print(f'{day} DATA UPLOADED SUCCESSFULY!') 

# BusStopTimeTable.delete(self=BusStopTimeTable)
# BusStopLineTable.delete()
# BusStop.delete()
# BusLine.delete()
# print('Successfuly cleared DB')

insert_bus_line()
insert_bus_stop()
insert_bus_stop_line()
insert_bus_stop_time()