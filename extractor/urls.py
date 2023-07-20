from django.urls import path
from .views import FileUploadView, dashboard

urlpatterns = [
    path('api/upload/', FileUploadView.as_view(), name='file-upload'),
    path('', dashboard, name='file-uploads'),
    path('dashboard/<int:pk>/', dashboard, name='dashboard2'),
]
