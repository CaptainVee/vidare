import io
import os
import PyPDF2
from pptx import Presentation

# def parse_pitch_deck(file_path):
#     file_extension = os.path.splitext(file_path)[1].lower()

#     if file_extension == '.pdf':
#         return parse_pdf(file_path)
#     elif file_extension == '.pptx':
#         return parse_pptx(file_path)
#     else:
#         raise ValueError("Unsupported file format")

def parse_pdf(file_path):
    extracted_text = ''
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()

    return extracted_text

def parse_pptx(file_path):
    extracted_text = ''
    presentation = Presentation(file_path)
    for slide in presentation.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    extracted_text += paragraph.text + '\n'

    return extracted_text
