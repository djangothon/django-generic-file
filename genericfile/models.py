from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey


class FileStore(models.Model):
    attachment = models.FileField(upload_to='genericfile')
    extension = models.TextField(null=True, blank=True)
    content_type = models.ForeignKey("contenttypes.ContentType", null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def get_name(self):
        return self.attachment.name.split('/')[-1]
