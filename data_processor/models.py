from django.db import models
from django.conf import settings

class UploadedFile(models.Model):
    file = models.FileField(upload_to=settings.MEDIA_ROOT)
    uploaded_at = models.DateTimeField(auto_now_add=True)