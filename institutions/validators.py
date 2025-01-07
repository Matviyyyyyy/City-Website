from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 20

def validate_image_size(file):
    if not file:
        raise ValidationError("No file selected.")
    if isinstance(file, UploadedFile):
        if file.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError("Розмір файлу не повинен перевищувати 20MB")

