from sre_constants import CATEGORY
from telnetlib import IP
from django.shortcuts import render, HttpResponse
from django.contrib.gis.geoip2 import GeoIP2

from .models import Category, Link
from datetime import datetime, timedelta
from django.utils import timezone



from django.utils.timezone import now

def home(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""

    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"
    
    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    
    g = GeoIP2()
    location = g.city(ip)
    location_country = location["country_name"]
    location_city = location["city"]
    timestamp  = datetime.now()
    categories= Category.objects.filter(name=ip)

    nombre= Link.objects.all()


    if not categories:
        notification = Category.objects.update_or_create(name=ip,device_type=device_type,browser_type=browser_type,browser_version=browser_version,os_type=os_type,os_version=os_version,location_country=location_country,location_city=location_city, timestamp=timestamp)
    elif categories:
        notification = Category.objects.filter(name=ip).update(name=ip,device_type=device_type,browser_type=browser_type,browser_version=browser_version,os_type=os_type,os_version=os_version,location_country=location_country,location_city=location_city)




    count = Category.objects.all(
            ).count() 
    countdos=Category.objects.filter(timestamp__date=datetime.today()).count()
    context = {
        "ip": ip,
        "count": count,
        "countdos": countdos,
        "nombre": nombre,
        "notification": notification,
        "categories": categories,
        "device_type": device_type,
        "browser_type": browser_type,
        "browser_version": browser_version,
        "os_type":os_type,
   
        "os_version":os_version,
        "location_country": location_country,
        "location_city": location_city
    }



    return render(request, "home.html", context)





def user(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""

    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"
    
    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    
    g = GeoIP2()
    location = g.city(ip)
    location_country = location["country_name"]
    location_city = location["city"]
    timestamp  = datetime.now()
    categories= Category.objects.all()

    nombre= Link.objects.all()
    count = Category.objects.all(
            ).count()


    context = {
        "ip": ip,
        "count": count,
        "nombre": nombre,
        "timestamp": timestamp,

        "categories": categories,
        "device_type": device_type,
        "browser_type": browser_type,
        "browser_version": browser_version,
        "os_type":os_type,
        "os_version":os_version,
        "location_country": location_country,
        "location_city": location_city
    }



    return render(request, "user.html", context)
