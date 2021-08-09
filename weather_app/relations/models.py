from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.html import mark_safe
import uuid


DELIVERY_TYPES = ((1, "plane"),
                  (2, "ship"),
                  (3, "car"),
                  (4, "legs"))


class BaseModel:
    create = models.DateTimeField('Create', auto_now_add=True, null=True)
    update = models.DateTimeField('Update', auto_now=True, null=True)

    class Meta:
        abstract = True


class Tag(BaseModel, models.Model):
    name = models.CharField(max_length=40, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ('name',)


class Category(BaseModel, MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField('Slug')
    tags = models.ManyToManyField(Tag, related_name='categories')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Goods(BaseModel, models.Model):
    name = models.CharField('Name', db_index=True, max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    price = models.IntegerField('Price', db_index=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image))
        return ""

    def __str__(self):
        return "£" + str(self.price) + " | " + self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'


class Cart(BaseModel, models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cart')
    goods = models.ManyToManyField(Goods, related_name='carts')
    delivery_type = models.IntegerField(choices=DELIVERY_TYPES)

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name = 'chum_bucket'
        verbose_name_plural = 'chum_buckets'
