from aluguel_de_salas.api import models, serializers
from rest_framework import filters, permissions, viewsets

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all().order_by('-created_at')
    serializer_class = serializers.CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['cpf']

class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all().order_by('-created_at')
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

class RentViewSet(viewsets.ModelViewSet):
    queryset = models.Rent.objects.all().order_by('-created_at')
    serializer_class = serializers.RentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = {
        'start': ['lte'],
        'end': ['gte'],
    }
