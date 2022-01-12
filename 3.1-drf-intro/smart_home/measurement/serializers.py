from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from .models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'creation_time', 'update_time']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
