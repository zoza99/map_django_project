from django.db import models


# Create your models here.
class Region_info(models.Model):
    region_name = models.CharField(max_length=50)
    region_lat = models.FloatField()
    region_lon = models.FloatField()


# class Data_weather(models.Model):
#     region_name = models.CharField(max_length=50)
#     #region_id =
#     period = models.CharField(max_length=50)
#     temp = models.FloatField()
#     pressure = models.IntegerField()
#     humidity = models.IntegerField()
#     wind_speed = models.FloatField()
#     wind_gust = models.FloatField()
#     rain = models.FloatField()
#     snow = models.FloatField()
#     #thunder =





