from django.contrib import admin
from .models import Category, Goods, Tag


class GoodsAdminInline(admin.StackedInline):
    model = Goods
    extra = 1


class CategoryAdminInline(admin.StackedInline):
    model = Category.tags.through
    extra = 1


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_slug = {'slug': ('name',)}
    filter_horizontal = ('tags',)
    inlines = [GoodsAdminInline]


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid']
    inlines = [CategoryAdminInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Tag, TagAdmin)
