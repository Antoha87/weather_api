from django.contrib import admin
from .models import Category,Goods


class GoodsAdminInline(admin.StackedInline):
    model = Goods
    extra = 1


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_slug = {'slug':('name',)}
    inlines = [GoodsAdminInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)