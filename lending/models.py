from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='название страницы')
    block = models.ManyToManyField('Block',
                                   through='BlockPosition',
                                   blank=True, verbose_name='изображение')

    def __str__(self):
        return f'{self.name}'


class BlockPosition(models.Model):
    page = models.ForeignKey('Page', on_delete=models.CASCADE, null=False, blank=False, verbose_name='страница')
    block = models.ForeignKey('Block', on_delete=models.CASCADE, null=False, blank=False, verbose_name='блок')
    block_position = models.PositiveSmallIntegerField(default=0, verbose_name='позиция блока')

    class Meta:
        ordering = ('block_position', )


class Block(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='название страницы')
    content_html = models.TextField(null=True, blank=True, verbose_name='контент html')
    image = models.ManyToManyField('Image',
                                   through='ImagePosition',
                                   blank=True, verbose_name='изображение')

    def __str__(self):
        return f'{self.name}'


class ImagePosition(models.Model):
    block = models.ForeignKey('Block', on_delete=models.CASCADE, null=False, blank=False, verbose_name='блок')
    image = models.ForeignKey('Image', on_delete=models.CASCADE, null=False, blank=False, verbose_name='изображение')
    image_position = models.PositiveSmallIntegerField(default=0, verbose_name='позиция изображения')


class Image(models.Model):
    image = models.ImageField(upload_to='img/content', null=True, blank=True, verbose_name='изображение')

    def __str__(self):
        return f'{self.image}'
