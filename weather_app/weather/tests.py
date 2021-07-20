from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.reverse import reverse


# Create your tests here.
class AuthenticationTest(APITestCase):
    fixtures = ['weather_app/fixtures/data.json']

    def test_not_authenticated_weather(self):
        response = self.client.get('/api/weather/')
        self.assertEqual(response.status_code, 401)

    def test_authenticated_weather(self):
        username = "bull.d"
        password = "123456"
        url = 'http://127.0.0.1:8000/api/weather/?format=json'
        url_auth = 'http://127.0.0.1:8000/api/token/?format=json'
        resp = self.client.post(url_auth, {'username': username, 'password': password}, format='json')
        # self.assertEqual(resp.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        print(resp.data)
        token = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = self.client.get(url)
        # Include an appropriate `Authorization:` header on all requests.
        data = [
    {
        "id": 7,
        "location": "Barcelona",
        "loc_time": "2021-07-19T10:14:00Z",
        "temperature": 27.0,
        "weather_icons": "['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png']"
    },
    {
        "id": 3,
        "location": "Kiev",
        "loc_time": "2021-07-19T11:14:00Z",
        "temperature": 29.0,
        "weather_icons": "['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0024_thunderstorms.png']"
    },
    {
        "id": 5,
        "location": "London",
        "loc_time": "2021-07-19T09:14:00Z",
        "temperature": 23.0,
        "weather_icons": "['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png']"
    },
    {
        "id": 6,
        "location": "Moscow",
        "loc_time": "2021-07-19T11:14:00Z",
        "temperature": 24.0,
        "weather_icons": "['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png']"
    },
    {
        "id": 1,
        "location": "New Delhi",
        "loc_time": "2021-07-19T13:44:00Z",
        "temperature": 26.0,
        "weather_icons": "['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0017_cloudy_with_light_rain.png']"
    },
    {
        "id": 4,
        "location": "Odessa",
        "loc_time": "2021-07-19T03:14:00Z",
        "temperature": 26.0,
        "weather_icons": "['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png']"
    },
    {
        "id": 2,
        "location": "Ottawa",
        "loc_time": "2021-07-19T04:14:00Z",
        "temperature": 19.0,
        "weather_icons": "['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png']"
    }
]
        print("DB\n")
        print(resp.content)
        self.assertJSONEqual(str(resp.content, encoding='utf8'), data)
