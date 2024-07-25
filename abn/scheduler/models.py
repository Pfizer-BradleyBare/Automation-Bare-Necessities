from datetime import datetime

from django.db import models


def get_upload_path(instance, filename):
    return f"_db_files/queued_methods/{filename[:-5]}/{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"


class QueuedMethod(models.Model):
    emails = models.CharField(max_length=100)
    phone_numbers = models.CharField(max_length=100)
    completion_time = models.DateTimeField()
    method_file = models.FileField(upload_to=get_upload_path, max_length=255)
