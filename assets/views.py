from rest_framework import viewsets
from .models import Asset
from .serializers import AssetSerializer
from rest_framework.permissions import IsAuthenticated

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all() 
    serializer_class = AssetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Asset.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
