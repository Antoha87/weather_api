from django.db import models


STATUS_CHOICES = ((1, 'New'), (2, 'Closed'))


class CurrencyData(models.Model):
    name = models.CharField('Cryptocurrency name', max_length=50)
    created = models.DateTimeField('Created')
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    data = models.JSONField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'currency data'
        verbose_name_plural = 'currencies data'
        ordering = ('id',)


class Currency(models.Model):
    name = models.CharField('Name', max_length=50)
    symbol = models.CharField('Symbol', max_length=50)
    price = models.FloatField('Price')
    change_30d = models.FloatField('Change 30d', null=True)
    change_60d = models.FloatField('Change 60d', null=True)
    change_90d = models.FloatField('Change 90d', null=True)
    max_supply = models.FloatField('Max supply', null=True)
    circulating_supply = models.FloatField('Circulating supply')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'
        ordering = ('id',)


class CurrencyAverage(models.Model):
    name = models.CharField('Name', max_length=50)
    avg_value = models.FloatField('Average value', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'currency average'
        verbose_name_plural = 'currencies averages'
        ordering = ('id',)


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.CharField('Email', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('id',)
