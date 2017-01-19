from django.db import models
from geoposition.fields import GeopositionField

import datetime

d = datetime.date.today()
s = datetime.datetime.now()
tv1 = s.time
td = datetime.timedelta(minutes=30)
tv = s + td

td2 = datetime.timedelta(days=7)

date1 = d
date2 = d + td2
yy = d.year
dd = d.day
mm = d.month

class Order(models.Model):
    current_point = GeopositionField(blank=False)
    current_date = models.DateField(blank=False)
    current_time = models.TimeField(blank=False)
    phone3 = models.CharField(max_length=11, blank=False)



