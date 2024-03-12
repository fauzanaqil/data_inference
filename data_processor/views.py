# display_data_project/data_processor/views.py
from django.shortcuts import render
from .forms import UploadFileForm
from . import script

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the uploaded file
            uploaded_file = request.FILES['file']
            chunk_size = 100000  # Adjust chunk size as needed for your system's memory
            # Call your data processing function with the uploaded file
            df = script.infer_and_convert_data_types(uploaded_file, chunk_size=chunk_size)
            # Get the data types after inference
            data_types = df.dtypes.to_dict()
            return render(request, 'data_processor/result.html', {'data_types': data_types})
    else:
        form = UploadFileForm()
    return render(request, 'data_processor/upload.html', {'form': form})
