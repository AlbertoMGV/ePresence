from tastypie.resources import ModelResource
from app.models import Aula
from tastypie.authorization import Authorization


class AulaResource(ModelResource):
	class Meta:
		queryset = Aula.objects.all()
		resource_name = 'Aula'
		authorization = Authorization()
