from rest_framework import serializers

from home.models import NavList


class NavListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavList
        fields = '__all__'
