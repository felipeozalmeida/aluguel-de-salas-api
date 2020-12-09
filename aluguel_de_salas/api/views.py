from rest_framework import permissions, viewsets
from aluguel_de_salas.api import models, serializers

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

    def get_queryset(self):
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)
        if self.queryset is not None and start is not None and end is not None:
            self.queryset = self.queryset.exclude(
                rent__end__gte=start, rent__start__lte=end)
        return self.queryset

class RentViewSet(viewsets.ModelViewSet):
    queryset = models.Rent.objects.all().order_by('-created_at')
    serializer_class = serializers.RentSerializer
    permission_classes = [permissions.IsAuthenticated]
