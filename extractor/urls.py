from django.urls import path
from .views import FileUploadView, ParsePitchDeckView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('parse/', ParsePitchDeckView.as_view(), name='parse-pitch-deck'),
]
