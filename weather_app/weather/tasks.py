import json
import requests
import logging
from celery import shared_task
from weather_app.celery import app as celery_app
from django.conf import settings
from .models import Weather

logger = logging.getLogger(__name__)

ACCESS_KEY = settings.ACCESS_KEY
CITIES = settings.CITIES


@celery_app.task(name="get all need currencies")
def get_weather():
    logger.info("RUN CELERY TASK - Get weather from api.weatherstack.com")
    for city in CITIES:

        params = {
            'access_key': ACCESS_KEY,
            'query': city
        }

        response = requests.get('http://api.weatherstack.com/current', params)
        if response.ok:
            data = json.loads(response.text)
            print(data)
            Weather.objects.get_or_create(location=data['location']['name'], loc_time=data['location']['localtime'],
                                          temperature=data['current']['temperature'],
                                          weather_icons=data['current']['weather_icons'])
            logger.info("OK")
        else:
            logger.critical('No response data from api.weatherstack.com! Please try later!')
