from rest_framework import serializers

from goods.models import Good, GoodImage


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'


class GoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodImage
        fields = ('image', 'index')


class GoodDetailSerializer(serializers.ModelSerializer):
    image = GoodImageSerializer(many=True)

    class Meta:
        model = Good
        fields = '__all__'
