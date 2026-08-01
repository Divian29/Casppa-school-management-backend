from rest_framework import serializers

from .models import School, SchoolClass, House


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            "id",
            "name",
        ]


class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = [
            "id",
            "name",
            "level",
        ]


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = [
            "id",
            "name",
            "color",
        ]