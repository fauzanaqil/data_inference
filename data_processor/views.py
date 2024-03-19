# # display_data_project/data_processor/views.py
# from django.shortcuts import render
# from .forms import UploadFileForm

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Process the uploaded file
#             uploaded_file = request.FILES['file']
#             chunk_size = 100000  
#             df = script.infer_and_convert_data_types(uploaded_file, chunk_size=chunk_size)
#             data_types = df.dtypes.to_dict()
#             return render(request, 'data_processor/result.html', {'data_types': data_types})
#     else:
#         form = UploadFileForm()
#     return render(request, 'data_processor/upload.html', {'form': form})

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UploadedFile
from .forms import UploadFileForm
from . import script
import os
from django.conf import settings

@api_view(['POST'])
def upload_file(request):
    file_obj = request.FILES.get('file')
    form = UploadFileForm(request.POST, request.FILES)
    if not file_obj and not form.is_valid():
        return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Save file to database
        uploaded_file = UploadedFile(file=file_obj)
        uploaded_file.save()

        # Access file name
        file_path = os.path.join(settings.MEDIA_ROOT, file_obj.name)
        
        if file_obj.size > 1000000:
            chunk_size = 100000  
            df = script.infer_and_convert_data_types(file_path, chunk_size=chunk_size)
        else:
            df = script.infer_and_convert_data_types(file_path)
        return Response({'message': 'File uploaded successfully', 'data_types': df}, status=status.HTTP_201_CREATED)
