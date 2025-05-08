from django.urls import path
from .views import DiagnosisAPIView


app_name = "model"

urlpatterns = [
    path('predict/', DiagnosisAPIView.as_view(), name='ai-diagnosis'),
]
