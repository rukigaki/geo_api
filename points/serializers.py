from rest_framework import serializers
from django.contrib.gis.geos import Point as GeoPoint

from .models import Point, Message


class PointSerializer(serializers.ModelSerializer):

    latitude = serializers.FloatField(default=0, write_only=True, initial=0)
    longitude = serializers.FloatField(default=0, write_only=True, initial=0)

    class Meta:
        model = Point
        fields = ("id", "latitude", "longitude", "created_at")

    def create(self, validated_data):
        lat = validated_data.pop("latitude")
        lon = validated_data.pop("longitude")
        validated_data["location"] = GeoPoint(lon, lat)

        return super().create(validated_data)


class MessageSerializer(serializers.ModelSerializer):
    text = serializers.CharField(initial="Привет, мир!")

    class Meta:
        model = Message
        fields = ("id", "point", "text", "created_at")

    def create(self, validated_data):
        return super().create(validated_data)
