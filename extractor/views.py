from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
import os
from django.views.generic import ListView, DetailView

from .models import ExtractedInfo, UploadedFile
from .serializers import UploadedFileSerializer, ExtractedInfoSerializer
from .utils import parse_pdf, parse_pptx


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request):
        file_serializer = UploadedFileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParsePitchDeckAPIView(APIView):
    serializer_class = ExtractedInfoSerializer

    def get(self, request, pk):
        file = UploadedFile.objects.get(pk=pk)
        file_path = file.file.name
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".pdf":
            extracted_text = parse_pdf(file_path)
        elif file_extension == ".pptx":
            extracted_text = parse_pptx(file_path)
        else:
            raise ValueError("Unsupported file format")

        file = UploadedFile.objects.get(file=file_path)
        extracted_info = ExtractedInfo.objects.create(file=file, content=extracted_text)
        serializer = self.serializer_class(extracted_info)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ParsePitchDeckView(ListView):
    model = UploadedFile
    context_object_name = "files"
    ordering = ["-uploaded_at"]
    paginate_by = 5
    template_name = "uploadedfile_list.html"


class ParsePitchDeckDetailView(DetailView):
    model = ExtractedInfo
    context_object_name = "file"
