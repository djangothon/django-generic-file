from django.conf.urls import url
from genericfile import views


urlpatterns = [
    url(r'^upload/$', views.FileUploadView.as_view(), name='genericfile_upload'),
    url(r'^list/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$', views.FileListView.as_view(), name='genericfile_list'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_file, name='genericfile_delete'),
]