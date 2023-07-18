from rest_framework import serializers
from .models import UploadedFile, ExtractedInfo

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('id', 'file', 'uploaded_at')
        read_only_fields = ('id', 'uploaded_at')


class ExtractedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedInfo
        fields = '__all__'