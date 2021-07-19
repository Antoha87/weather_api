from django.db import models


class BaseModel(models.Model):
    create = models.DateTimeField('Create', auto_now_add=True, null=True)
    update = models.DateTimeField('Update', auto_now=True, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Category(BaseModel):
    slug = models.SlugField('Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name',)


class Goods(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    price = models.IntegerField('Price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('name',)