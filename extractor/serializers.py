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

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['get_name'] = instance.get_name
        data['get_file_size'] = instance.get_file_size
        return data