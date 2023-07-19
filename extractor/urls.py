from django.urls import path
from .views import FileUploadView, ParsePitchDeckAPIView, ParsePitchDeckView, ParsePitchDeckDetailView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('', ParsePitchDeckView.as_view(), name='file-uploads'),
    path('file/<int:pk>/', ParsePitchDeckDetailView.as_view(), name='file-upload-details'),
    path('parse/<int:pk>/', ParsePitchDeckAPIView.as_view(), name='parse-pitch-deck'),
]
