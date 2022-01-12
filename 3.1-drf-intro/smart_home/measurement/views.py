# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorCreateSerializer


class SensorCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorCreateSerializer


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
