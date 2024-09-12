import pandas as pd
import os
from django.conf import settings

def extract_data_from_file(file):
    file_extension = os.path.splitext(file.name)[1]

    # Save the file temporarily
    file_path = os.path.join(settings.MEDIA_ROOT, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    try:
        # Process CSV/Excel files
        if file_extension == '.csv':
            df = pd.read_csv(file_path)
        elif file_extension == '.xlsx':
            df = pd.read_excel(file_path)

        return df  # Return the extracted DataFrame for column selection

    finally:
        # Delete the file after processing
        if os.path.exists(file_path):
            os.remove(file_path)
