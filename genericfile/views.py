from django.core.urlresolvers import reverse
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from genericfile.forms import FileUploadForm
from genericfile.models import FileStore


class FileUploadView(CreateView):
    model = FileStore
    form_class = FileUploadForm
    object = None

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return JsonResponse({
            'status': 'success',
            'id': self.object.id,
            'name': self.object.attachment.name.split('/')[-1],
            'path': self.object.attachment.url,
            'delete_url': reverse('genericfile_delete', args=[self.object.id]),
            'size': self.object.attachment.size
        })

    def form_invalid(self, form):
        return JsonResponse({
            'status': 'error',
            'jquery-upload-file-error': 'File Upload Error'
        })


class FileListView(ListView):

    def get_queryset(self):
        queryset = FileStore.objects.filter(**self.kwargs)
        if 'type' in self.request.GET:
            queryset = queryset.filter(extension__contains='"type": "'+self.request.GET['type']+'"')
        return queryset

    def render_to_response(self, context, **response_kwargs):
        file_list = []
        for file_obj in context['object_list']:
            file_list.append({
                'id': file_obj.id,
                'name': file_obj.attachment.name.split('/')[-1],
                'path': file_obj.attachment.url,
                'delete_url': reverse('genericfile_delete', args=[file_obj.id]),
                'size': file_obj.attachment.size
            })
        return JsonResponse(file_list, safe=False)


@require_POST
def delete_file(request, pk):
    f = FileStore.objects.get(id=pk)
    f.attachment.delete()
    f.delete()
    return JsonResponse({'status': 'success'})


def update_genericfile(POST, obj):
    ids = POST['genericfile_ids'].split(',')
    for id in ids:
        fs = FileStore.objects.get(id=id)
        fs.content_object = obj
        fs.save()