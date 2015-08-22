from django import template
from django.contrib.contenttypes.models import ContentType
from genericfile.models import FileStore

register = template.Library()


@register.inclusion_tag('genericfile/filestore_form.html')
def get_genericfile_form(**kwargs):
    data = {}
    host_model = kwargs.get('host_model')
    if host_model is not None:
        data['content_type'] = ContentType.objects.get_for_model(host_model)
    host_object = kwargs.get('host_object')
    if host_object is not None:
        data['content_type'] = ContentType.objects.get_for_model(host_object)
        data['host_object'] = host_object
    return data


@register.assignment_tag
def get_genericfile_list(**kwargs):
    host_object = kwargs.get('host_object')
    content_type = ContentType.objects.get_for_model(host_object)
    return FileStore.objects.filter(content_type=content_type, object_id=host_object.id)