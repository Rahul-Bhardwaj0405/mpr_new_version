from django.db import models

# Create your models here.

from django.db import models

class ExtractedData(models.Model):
    selected_columns_data = models.JSONField()  # Stores only the selected columns as JSON

    def __str__(self):
        return f"Data with ID {self.id}"
