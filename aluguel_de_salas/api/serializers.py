from rest_framework import serializers
from aluguel_de_salas.api import models

# Create your serializers here.
class BaseSerializer():
    fields = ['comments', 'created_at', 'updated_at']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Customer
        fields = [
            'name', 'cpf', 'birthday', 'phone', 'email',
        ] + BaseSerializer.fields

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Room
        fields = [
            'name', 'size', 'capacity', 'description', 'price',
        ] + BaseSerializer.fields

class RentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Rent
        fields = [
            'customer', 'room', 'value', 'start', 'end',
        ] + BaseSerializer.fields
