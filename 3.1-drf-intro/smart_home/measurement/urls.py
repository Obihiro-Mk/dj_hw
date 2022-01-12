from django.urls import path

from .views import SensorCreateView, MeasurementCreateView, SensorUpdateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),

]
