from django.urls import path, include
from . import views

urlpatterns = [
    path('upload/', views.upload_file),
    # path('data-types/', name='data_types'),
    # path('api/', include('data_processor.urls')),
]