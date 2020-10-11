from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django import forms
from .models import Airsensorinfo, Gassensorinfo, Motionsensorinfo, Rainsensorinfo, Tempsensorinfo, Userinfo
import datetime 
import pickle, sys, time

# Create your views here.
def index(request) :   

    #db에서 꺼내는 문장 - db의 가장 마지막 record 꺼내옴!
    air_row = Airsensorinfo.objects.filter(user = 1).last()
    motion_row = Motionsensorinfo.objects.filter(user = 1).last()
    temp_row = Tempsensorinfo.objects.filter(user = 1).last()
    rain_row = Rainsensorinfo.objects.filter(user = 1).last()
    gas_row = Gassensorinfo.objects.filter(user = 1).last()

    if air_row is None :   
        air_condition = 0
    else :
        air_condition = air_row.situation

    if motion_row is None :   
        motion_condition = 0
    else :
        motion_condition = motion_row.situation

    if temp_row is None :   
        temp_condition = 0
    else :
        temp_condition = temp_row.situation

    if rain_row is None :   
        rain_condition = 0
    else :
        rain_condition = rain_row.situation

    if gas_row is None :   
        gas_condition = 0
    else :
        gas_condition = gas_row.situation
    
    #수동 제어 공간 
    if request.method == "GET":
        temp_condition_recv = request.GET.get('temp_condition', None) #html form에서 수정된 condition 값을 받아옴, 없을 시 None
        gas_condition_recv = request.GET.get('gas_condition', None)
        air_condition_recv = request.GET.get('air_condition', None)
        motion_condition_recv = request.GET.get('motion_condition', None)
        rain_condition_recv = request.GET.get('rain_condition', None)

        temp_is_auto_recv = request.GET.get('temp_is_auto', None)
        gas_is_auto_recv = request.GET.get('gas_is_auto', None)
        air_is_auto_recv = request.GET.get('air_is_auto', None)
        motion_is_auto_recv = request.GET.get('motion_is_auto', None)
        rain_is_auto_recv = request.GET.get('rain_is_auto', None)
            
        if temp_condition_recv != temp_condition and temp_condition_recv != None: #수정된 값이 기존 값과 다르고, None이 아닐경우, 
            Tempsensorinfo.objects.create(
                user = temp_row.user, 
                situation = temp_condition_recv, 
                temp_value = temp_row.temp_value,
                humid_value = temp_row.humid_value,
                is_auto = temp_is_auto_recv
            )
            
            temp_row = Tempsensorinfo.objects.filter(user = temp_row.user).last()
        
        if gas_condition_recv != gas_condition and gas_condition_recv != None:
            Gassensorinfo.objects.create(
                user = gas_row.user, 
                situation = gas_condition_recv, 
                gas_value = gas_row.gas_value,
                is_auto = gas_is_auto_recv
            )
            gas_row = Gassensorinfo.objects.filter(user = gas_row.user).last()

        if air_condition_recv != air_condition and air_condition_recv != None:
            Airsensorinfo.objects.create(
                user = air_row.user, 
                situation = air_condition_recv, 
                air1_value = air_row.air1_value,
                air2_value = air_row.air2_value,
                is_auto = air_is_auto_recv
            )
            air_row = Airsensorinfo.objects.filter(user = air_row.user).last()

        if rain_condition_recv != rain_condition and rain_condition_recv != None:
            Rainsensorinfo.objects.create(
                user = rain_row.user, 
                situation = rain_condition_recv, 
                is_auto = rain_is_auto_recv,
                rain_value = rain_row.rain_value
            )
            rain_row = Rainsensorinfo.objects.filter(user = rain_row.user).last()

        if motion_condition_recv != motion_condition and motion_condition_recv != None:
            Motionsensorinfo.objects.create(
                user = motion_row.user, 
                situation = motion_condition_recv, 
                is_auto = motion_is_auto_recv,
                motion_value = motion_row.motion_value
            
            )
            motion_row = Motionsensorinfo.objects.filter(user = motion_row.user).last()

        
    sensor = {
        'air' : air_row,
        'motion' : motion_row,
        'temp' : temp_row,
        'rain' : rain_row,
        'gas' : gas_row,
    }

    return render(request, 'smarthome/main.html', sensor)       


def airconditioner(request, temp) :
    temp_row = Tempsensorinfo.objects.filter(user = 1).last()
    temp_condition = temp_row.situation

    if request.method == "GET":
        temp_condition_recv = request.GET.get('temp_condition', None) 
        temp_is_auto_recv = request.GET.get('temp_is_auto', None) 

        # if temp_condition_recv != temp_condition and temp_condition_recv != None:
        if temp_is_auto_recv != None:
            Tempsensorinfo.objects.create(
                user = temp_row.user, 
                situation = temp_row.situation, 
                temp_value = temp_row.temp_value,
                humid_value = temp_row.humid_value,
                is_auto = temp_is_auto_recv
            )

        if temp_condition_recv != temp_condition and temp_condition_recv != None:
            Tempsensorinfo.objects.create(
                user = temp_row.user, 
                situation = temp_condition_recv, 
                temp_value = temp_row.temp_value,
                humid_value = temp_row.humid_value,
                is_auto = 0
            )

        temp_row = Tempsensorinfo.objects.filter(user = temp_row.user).last()
    
    context = {'temp' : temp_row}
    return render(request, 'smarthome/aircondtioner.html', context)

def aircleaner(request, air) :
    air_row = Airsensorinfo.objects.filter(user = 1).last()
    air_condition = air_row.situation


    if request.method == "GET":
        air_condition_recv = request.GET.get('air_condition', None) 
        air_is_auto_recv = request.GET.get('air_is_auto', None) 

        if air_is_auto_recv != None:
            Airsensorinfo.objects.create(
                user = air_row.user, 
                situation = air_row.situation, 
                air1_value = air_row.air1_value,
                air2_value = air_row.air2_value,
                is_auto = air_is_auto_recv
            )

        if air_condition_recv != air_condition and air_condition_recv != None:
            Airsensorinfo.objects.create(
                user = air_row.user, 
                situation = air_condition_recv, 
                air1_value = air_row.air1_value,
                air2_value = air_row.air2_value,
                is_auto = 0
            )

        air_row = Airsensorinfo.objects.filter(user = air_row.user).last()
    
    context = {'air' : air_row}
    return render(request, 'smarthome/aircleaner.html', context)

def gascooker(request, gas) :
    gas_row = Gassensorinfo.objects.filter(user = 1).last()
    gas_condition = gas_row.situation


    if request.method == "GET":
        gas_condition_recv = request.GET.get('gas_condition', None) 
        gas_is_auto_recv = request.GET.get('gas_is_auto', None) 

        if gas_is_auto_recv != None:
            Gassensorinfo.objects.create(
                user = gas_row.user, 
                situation = gas_row.situation, 
                gas_value = gas_row.gas_value,
                is_auto = gas_is_auto_recv
            )

        if gas_condition_recv != gas_condition and gas_condition_recv != None:
            Gassensorinfo.objects.create(
                user = gas_row.user, 
                situation = gas_condition_recv, 
                gas_value = gas_row.gas_value,
                is_auto = 0
            )

        gas_row = Gassensorinfo.objects.filter(user = gas_row.user).last()
    
    context = {'gas' : gas_row}
    return render(request, 'smarthome/gas.html', context) 

def window(request, rain) :
    rain_row = Rainsensorinfo.objects.filter(user = 1).last()
    rain_condition = rain_row.situation
    temp_row = Tempsensorinfo.objects.filter(user = 1).last()
    temp_humid = temp_row.humid_value

    if request.method == "GET":
        rain_condition_recv = request.GET.get('rain_condition', None) 
        rain_is_auto_recv = request.GET.get('rain_is_auto', None) 

        if rain_is_auto_recv != None:
            Rainsensorinfo.objects.create(
                user = rain_row.user, 
                situation = rain_row.situation, 
                is_auto = rain_is_auto_recv,
                rain_value = rain_row.rain_value
            )

        if rain_condition_recv != rain_condition and rain_condition_recv != None:
            Rainsensorinfo.objects.create(
                user = rain_row.user, 
                situation = rain_condition_recv, 
                is_auto = 0,
                rain_value = rain_row.rain_value
            )

        rain_row = Rainsensorinfo.objects.filter(user = rain_row.user).last()
    
    context = {'rain' : rain_row, 'humid' : temp_humid}
    return render(request, 'smarthome/window.html', context)

def lamp(request, motion) :
    motion_row = Motionsensorinfo.objects.filter(user = 1).last()
    motion_condition = motion_row.situation

    if request.method == "GET":
        motion_condition_recv = request.GET.get('motion_condition', None) 
        motion_is_auto_recv = request.GET.get('motion_is_auto', None) 

        if motion_is_auto_recv != None:
             Motionsensorinfo.objects.create(
                user = motion_row.user, 
                situation = motion_row.situation, 
                is_auto = motion_is_auto_recv,
                motion_value = motion_row.motion_value
            )

        if motion_condition_recv != motion_condition and motion_condition_recv != None:
             Motionsensorinfo.objects.create(
                user = motion_row.user, 
                situation = motion_condition_recv, 
                is_auto = 0,
                motion_value = motion_row.motion_value
            )

        motion_row = Motionsensorinfo.objects.filter(user = motion_row.user).last()
    
    context = {'motion' : motion_row} 
    return render(request, 'smarthome/lamp.html', context)