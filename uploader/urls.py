from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.file_upload_view, name='file-upload'),
    path('select-columns/', views.select_columns_view, name='select-columns'),
    path('success/', views.success_view, name='success'),
]
