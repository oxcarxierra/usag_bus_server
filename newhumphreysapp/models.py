from django.db import models

# Create your models here.

class BusStop(models.Model):
    code = models.CharField(max_length=3, unique=True, null=False, primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=7,null=False, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=7,null=False, default=0)
    def __str__(self):
        return '%s: %s' % (self.code, self.name)
        
class BusLine(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    length = models.IntegerField(default=0)
    
class BusStopLineTable(models.Model):
    bus_stop = models.ForeignKey(BusStop, on_delete=models.CASCADE, related_name='this_stop')
    bus_line = models.ForeignKey(BusLine, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    # class Meta:
    #     unique_together = [
    #         ('order', 'bus_line')
    #     ]

class BusStopTimeTable(models.Model):
    bus_stop_line_table = models.ForeignKey(BusStopLineTable, on_delete=models.CASCADE)
    arrival_time = models.CharField(max_length=4, null=False)
    day = models.CharField(null=False, default='reg', max_length=3)
    # weekend = models.BooleanField(null=False, default=False)
