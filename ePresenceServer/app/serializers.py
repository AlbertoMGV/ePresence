from app.models import Aula
from rest_framework import serializers


class AulaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aula
        fields = ['id', 'personas', 'estado', 'hora_in', 'hora_out']