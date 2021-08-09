from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Shawarma(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField()
    price = models.FloatField()
    ingredients = models.ManyToManyField(Ingredient, related_name='shawarmas')

    def __str__(self):
        return self.name
