from hunter_bank.models import Offer, Client
from hunter_bank.serializers import OfferSerializer, ClientSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import filters


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ("ID", "client_create", "client_update", "client_family", "client_birthday", "client_phone_number",
                     "client_passport_number", "client_scoring_point")


@api_view
def api_root(request, format=None):
    return Response({
        'offers': reverse('offer-list', request=request, format=format),
        'clients': reverse('client-list', request=request, format=format)
    })
