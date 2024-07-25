from datetime import datetime

from django.db import models


def get_upload_path(instance, filename):
    print(filename[:-5])
    return f"_db_files/queued_methods/{filename[:-5]}/{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"


class QueuedMethod(models.Model):
    file = models.FileField(upload_to=get_upload_path, max_length=255)
