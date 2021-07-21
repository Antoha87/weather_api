from django.db import models
import uuid


class BaseModel(models.Model):
    create = models.DateTimeField('Create', auto_now_add=True, null=True)
    update = models.DateTimeField('Update', auto_now=True, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(max_length=40, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ('name',)


class Category(BaseModel):
    slug = models.SlugField('Slug')
    tags = models.ManyToManyField(Tag, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name',)


class Goods(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    price = models.IntegerField('Price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('name',)
