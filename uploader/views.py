from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import ExtractedData
from .tasks import extract_data_from_file
import pandas as pd

def file_upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            folder_files = request.FILES.getlist('folder')
            for f in folder_files:
                # Extract data and store it in session for column selection
                file_data = extract_data_from_file(f)
                request.session['file_data'] = file_data.to_dict(orient='records')  # Store extracted data in session
                request.session['columns'] = list(file_data.columns)  # Store columns for user selection
            return redirect('select-columns')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

def select_columns_view(request):
    columns = request.session.get('columns', [])
    file_data = request.session.get('file_data', [])
    
    if request.method == 'POST':
        selected_columns = request.POST.getlist('selected_columns')
        
        # Filter the data to include only selected columns
        selected_data = [{col: row[col] for col in selected_columns} for row in file_data]
        
        # Save each row of selected column data into the ExtractedData model
        for row in selected_data:
            ExtractedData.objects.create(selected_columns_data=row)
        
        return redirect('success')

    return render(request, 'select_columns.html', {'columns': columns})

def success_view(request):
    extracted_data = ExtractedData.objects.all()
    return render(request, 'success.html', {'extracted_data': extracted_data})
