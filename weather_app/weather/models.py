from django.db import models


class BaseModel(models.Model):
    create = models.DateTimeField('Create', auto_now_add=True)
    update = models.DateTimeField('Update', auto_now=True)


class Weather(BaseModel):
    location = models.CharField('location', max_length=20)
    loc_time = models.DateTimeField('location time')
    temperature = models.FloatField('temperature')
    weather_icons = models.CharField('weather icons', max_length=255)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'weather'
        verbose_name_plural = 'weathers'
        ordering = ('location',)



# Create your models here.
