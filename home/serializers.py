from rest_framework import serializers

from home.models import NavList, PanelContents, Panel


class NavListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavList
        fields = '__all__'


class PanelContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanelContents
        fields = '__all__'


class PanelSerializer(serializers.ModelSerializer):
    panelContents = PanelContentsSerializer(many=True)

    class Meta:
        model = Panel
        fields = '__all__'
