from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.file.name


class ExtractedInfo(models.Model):
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    slide_title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    metadata = models.JSONField(blank=True, null=True)
    extracted_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_name(self):
        return self.file.file.name

    @property
    def get_file_size(self):
        size_in_bytes = self.file.file.size
        size_in_kb = size_in_bytes / 1024
        return f"{size_in_kb:.1f} KB"

