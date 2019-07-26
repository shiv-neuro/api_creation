from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
        authentication = BasicAuthentication()