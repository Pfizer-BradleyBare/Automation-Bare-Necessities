from django.db import models


def get_upload_path(instance, filename):
    print(filename[:-5])
    return f"abn/files/queued_methods/{filename[:-5]}/{filename}"


class QueuedMethod(models.Model):
    file = models.FileField(upload_to=get_upload_path)
