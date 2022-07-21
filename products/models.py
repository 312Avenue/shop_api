from gettext import Catalog
from django.db import models
from slugify import slugify

# Catalog
class ProdType(models.Model):
    name = models.CharField(verbose_name='Название', max_length=155)
    slug = models.SlugField(verbose_name='', blank=True, primary_key=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Catalog(models.Model):
    name = models.CharField(verbose_name='Название', max_length=155)
    description = models.TextField(verbose_name='Описание')
    prod_type = models.ForeignKey(ProdType, verbose_name='Тип', on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Фотография')
    color = models.CharField(verbose_name='Цвет', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прокдукт'
        verbose_name_plural = 'Продукты'


class Price(models.Model):
    prod_name = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='price')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=0)
    discount = models.PositiveSmallIntegerField(verbose_name='Скидка', default=0)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.prod_name}: {self.price}'

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Size(models.Model):
    prod_name = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='size')
    width = models.CharField(verbose_name='Ширина', max_length=155)
    deep = models.CharField(verbose_name='Глубина', max_length=155)
    heigth = models.CharField(verbose_name='Высота', max_length=155)

    def __str__(self):
        return f'{self.prod_name}'

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Images(models.Model):
    prod_name = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(verbose_name='Фотография')

    def __str__(self):
        return f'{self.prod_name}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Tags(models.Model):
    prod_name = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='tags')
    tags = models.CharField(verbose_name='', max_length=155)

    def __str__(self):
        return f'{self.prod_name}: {self.tags}'

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

