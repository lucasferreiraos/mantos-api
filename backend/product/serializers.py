from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Image, Product


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.ImageField()

    class Meta:
        model = Product
        fields = [
            'title',
            'slug',
            'description',
            'price',
            'thumbnail',
            'images',
        ]

    def create(self, validated_data):
        data = validated_data.copy()
        data.pop('images')

        images_data = self.context.get('request').data.pop('images')
        try:
            product = Product.objects.create(**data)
        except TypeError:
            msg = (_('Pode não, viu!?'))
            raise TypeError(msg)

        try:
            for image_data in images_data:
                image, created = Image.objects.get_or_create(image=image_data)
                product.images.add(image)

            return product
        except TypeError:
            product = Product.objects.get(pk=product.id)
            product.delete()
            msg = (_('tmb n pode'))
            raise TypeError(msg)
        return product

    def update(self, instance, validated_data):
        try:
            images_data = self.context.get('request').data.pop('images')
        except Exception:
            images_data = None

        if images_data is not None:
            image_instance_list = list()

            for image_data in images_data:
                image, created = Image.objects.get_or_create(image=image_data)
                image_instance_list.append(image)

            instance.images.set(image_instance_list)

        instance.save()
        return instance
        # return super().update(instance, validated_data)
