import os
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

from .models import ExtractedInfo
from .serializers import UploadedFileSerializer, ExtractedInfoSerializer
from .utils import parse_pdf, parse_pptx
from .forms import FileUploadForm


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request):
        file_serializer = UploadedFileSerializer(data=request.FILES)

        if file_serializer.is_valid():
            file = file_serializer.save()
            file_path = file.file.name
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension == ".pdf":
                extracted_text = parse_pdf(file_path)
            elif file_extension == ".pptx":
                extracted_text = parse_pptx(file_path)
            else:
                raise ValueError("Unsupported file format")
            print(extracted_text)

            extracted_info = ExtractedInfo.objects.create(
                file=file,
                title=extracted_text.get("Title", ""),
                content=extracted_text.get("Content", ""),
                no_of_pages=extracted_text.get("no_of_pages", ""),
            )
            serializer = ExtractedInfoSerializer(extracted_info)
            # serializer["file"] =extracted_info.file
            # serializer[]
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def dashboard(request):
    extractes = ExtractedInfo.objects.all()
    extracted_info = ""
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Call the API class to process the uploaded file
            api_view = FileUploadView()
            response = api_view.post(request)

            # Pass the extracted info to the template
            extracted_info = response.data
    form = FileUploadForm()
    context = {"form": form, "extracted_info": extracted_info, "extractes": extractes}
    return render(request, "extractor/dashboard.html", context)

def dashboard2(request, pk):
    extractes = ExtractedInfo.objects.all()
    extracted_info = ExtractedInfo.objects.get(pk=pk)
    context = {"extracted_info": extracted_info, "extractes": extractes}
    return render(request, "extractor/dashboard.html", context)