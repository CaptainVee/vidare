from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status

from .models import UploadedFile
from .serializers import UploadedFileSerializer

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        file_serializer = UploadedFileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParsePitchDeckView(APIView):
    pass
