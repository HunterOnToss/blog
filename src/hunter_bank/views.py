from hunter_bank.models import Offer
from hunter_bank.serializers import OfferSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view
def api_root(request, format=None):
    return Response({
        'offers': reverse('offer-list', request=request, format=format)
    })
