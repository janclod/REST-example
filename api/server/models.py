from django.contrib.gis.db import models


class Municipality(models.Model):
    name = models.CharField(max_length=50)
    coordinates = models.MultiPolygonField()
    crs = models.CharField()
    collection = models.CharField()

    def __str__(self):
        return self.name
