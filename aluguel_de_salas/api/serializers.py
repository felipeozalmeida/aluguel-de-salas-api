from rest_framework import serializers
from aluguel_de_salas.api import models

# Create your serializers here.
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Customer
        fields = [
            'url', 'name', 'cpf', 'birthday', 'phone', 'email', 'comments',
            'created_at', 'updated_at',
        ]

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Room
        fields = [
            'url', 'name', 'size', 'capacity', 'description', 'price', 'comments',
            'created_at', 'updated_at',
        ]

class RentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Rent
        fields = [
            'url', 'customer', 'room', 'value', 'start', 'end', 'comments',
            'created_at', 'updated_at',
        ]
