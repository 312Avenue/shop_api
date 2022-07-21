from rest_framework import serializers

from .models import *

# Catalog
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('width', 'deep', 'heigth')
    

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('price', 'discount')


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('tags',)


class ProdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdType
        fields = ('name',)


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('images',)


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = "__all__"

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['old price'] = PriceSerializer(instance.price.filter(prod_name=instance.id), many=True).data
        if dict(represent['old price'][0])['discount']:
            price = dict(PriceSerializer(instance.price.filter(prod_name=instance.id), many=True).data[0])
            represent['old price'] = price['price']
            represent['discount'] = price['discount']
            represent['new price'] = str((int(price['price']) - round(int(price['price']) * (price['discount'] / 100))))[:-1] + '0'
        represent['size'] = SizeSerializer(instance.size.all(), many=True).data
        represent['images'] = [dict(i)['images'] for i in(ImagesSerializer(instance.images.filter(prod_name=instance.id), many=True).data)]
        represent['tags'] = TagsSerializer(instance.tags.all(), many=True).data
        return represent


# Advatages
class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ('title', 'body')


# Econom
class EconomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Econom
        fields = ('title', 'body')


# Furniture
class FurnitureCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureCategories
        fields = ('name',)


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ('fur_type', 'img')

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['categoties'] = [dict(i)['name'] for i in FurnitureCategoriesSerializer(instance.categories.filter(furniture=instance.id), many=True).data]
        return represent


# Pluses
class PlusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pluses
        fields = ('img', 'title', 'body')


# Profit
class ProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profit
        fields = ('img', 'title', 'body')