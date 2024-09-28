from django.urls import path

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
]

from .views import SensorListCreateView, SensorUpdateView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('sensors/<int:pk>/update/', SensorUpdateView.as_view(), name='sensor-update'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
]
