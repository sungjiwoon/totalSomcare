# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airsensorinfo(models.Model):
    user = models.ForeignKey('Userinfo', models.CASCADE)
    situation = models.IntegerField(blank=True, null=True)
    is_auto = models.IntegerField()
    air1_value = models.FloatField(blank=True, null=True)
    air2_value = models.FloatField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'airSensorInfo'


class Gassensorinfo(models.Model):
    user = models.ForeignKey('Userinfo', models.CASCADE)
    situation = models.IntegerField(blank=True, null=True)
    is_auto = models.IntegerField()
    gas_value = models.FloatField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'gasSensorInfo'


class Motionsensorinfo(models.Model):
    user = models.ForeignKey('Userinfo', models.CASCADE)
    situation = models.IntegerField(blank=True, null=True)
    is_auto = models.IntegerField()
    motion_value = models.FloatField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'motionSensorInfo'


class Rainsensorinfo(models.Model):
    user = models.ForeignKey('Userinfo', models.CASCADE)
    situation = models.IntegerField(blank=True, null=True)
    is_auto = models.IntegerField()
    rain_value = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'rainSensorInfo'


class Tempsensorinfo(models.Model):
    user = models.ForeignKey('Userinfo', models.CASCADE)
    situation = models.IntegerField(blank=True, null=True)
    is_auto = models.IntegerField()
    temp_value = models.FloatField(blank=True, null=True)
    humid_value = models.FloatField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'tempSensorInfo'

class Userinfo(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'userInfo'