from django.contrib import admin
from .models import Category, Goods, Tag, Cart
from mptt.admin import DraggableMPTTAdmin


class GoodsAdminInline(admin.StackedInline):
    model = Goods
    extra = 1


class CategoryAdminInline(admin.StackedInline):
    model = Category.tags.through
    extra = 1


class CartAdminInline(admin.StackedInline):
    model = Cart.goods.through
    extra = 1


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


class CartAdmin(admin.ModelAdmin):
    filter_vertical = ('goods',)
    list_display = ['owner', 'delivery_type']


class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_slug = {'slug': ('name',)}
    filter_horizontal = ('tags',)
    inlines = [GoodsAdminInline]
    mptt_level_indent = 3
    list_display = ['name']
    list_display_links = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid']
    inlines = [CategoryAdminInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Cart, CartAdmin)