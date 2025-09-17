from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
       car_Name=models.CharField(max_length=10) 
       car_ID=models.IntegerField(primary_key=True)
       fuel_Type=models.CharField(max_length=10)
       color=models.CharField(max_length=10)
       mileage=models.IntegerField()
class Car_DBAdmin(admin.ModelAdmin):
      list_display=["car_Name","car_ID","fuel_Type","color","mileage"]

