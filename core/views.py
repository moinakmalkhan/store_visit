from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import StoreSerializer, VisitSerializer
from .authentication import PhoneAuthentication
from .permissions import IsEmployee


class StoreListView(ListAPIView):
    authentication_classes = [PhoneAuthentication]
    permission_classes = [IsEmployee]
    serializer_class = StoreSerializer

    def get_queryset(self):
        return self.request.employee.stores.all()


class VisitCreateView(ListCreateAPIView):
    authentication_classes = [PhoneAuthentication]
    permission_classes = [IsEmployee]
    serializer_class = VisitSerializer

    def get_queryset(self):
        return self.request.employee.visits.all()
