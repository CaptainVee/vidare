from django.urls import path
from .views import FileUploadView, dashboard, dashboard2

urlpatterns = [
    path('api/upload/', FileUploadView.as_view(), name='file-upload'),
    path('', dashboard, name='dashboard'),
    path('dashboard/<int:pk>/', dashboard2, name='dashboard2'),
]
