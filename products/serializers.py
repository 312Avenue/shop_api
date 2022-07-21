from rest_framework import serializers

from .models import Catalog, Size, Price, Tags, ProdType, Images

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['width', 'deep', 'heigth']
    

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['price', 'discount']


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['tags']


class ProdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdType
        fields = ['name']


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['images']


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['old price'] = PriceSerializer(instance.price.filter(prod_name=instance.id), many=True).data
        if dict(rep['old price'][0])['discount']:
            price = dict(PriceSerializer(instance.price.filter(prod_name=instance.id), many=True).data[0])
            rep['old price'] = price['price']
            rep['discount'] = price['discount']
            rep['new price'] = str(float(price['price']) - (float(price['price']) * (price['discount'] / 100)))
        rep['size'] = SizeSerializer(instance.size.all(), many=True).data
        rep['images'] = ImagesSerializer(instance.images.all(), many=True).data
        rep['tags'] = TagsSerializer(instance.tags.all(), many=True).data
        return rep