import json
from django import forms
from django.contrib.contenttypes.models import ContentType
from genericfile.models import FileStore


class FileUploadForm(forms.ModelForm):
    content_type = forms.CharField(required=False, widget=forms.HiddenInput())
    object_id = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = FileStore
        fields = ('attachment', 'content_type', 'object_id', 'extension')

    def clean_content_type(self):
        content_type_id = self.data.get('content_type')
        if content_type_id is not None:
            return ContentType.objects.get(id=content_type_id)

    def clean_extension(self):
        extension = self.data.get('extension')
        if extension is not None:
            try:
                data_dict = json.loads(extension)
                return json.dumps(data_dict)
            except ValueError, e:
                raise forms.ValidationError("Invalid json format for the field `extension`")
