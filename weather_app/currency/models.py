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
    change_30d = models.FloatField('Change 30d')
    change_60d = models.FloatField('Change 60d')
    change_90d = models.FloatField('Change 90d')
    max_supply = models.FloatField('Max supply', null=True)
    circulating_supply = models.FloatField('Circulating supply')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'
        ordering = ('id',)
