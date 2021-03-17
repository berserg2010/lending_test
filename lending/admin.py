from django.contrib import admin

from .models import Page, BlockPosition, Block, ImagePosition, Image


class BlockPositionInline(admin.StackedInline):
    model = BlockPosition
    extra = 0


class ImagePositionInline(admin.StackedInline):
    model = ImagePosition
    extra = 0


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = (BlockPositionInline, )


@admin.register(BlockPosition)
class BlockPositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    inlines = (ImagePositionInline,)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
