from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ExtractedInfo(models.Model):
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    slide_title = models.CharField(max_length=255)
    content = models.TextField()
    metadata = models.JSONField()
    extracted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slide_title
