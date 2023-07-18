from django.contrib import admin
from .models import UploadedFile, ExtractedInfo

# Register your models here.
admin.site.register(UploadedFile)
admin.site.register(ExtractedInfo)