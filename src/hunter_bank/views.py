# coding=utf-8
from hunter_bank.models import Offer, Client, CreditApplication
from hunter_bank.serializers import OfferSerializer, ClientSerializer, CreditApplicationSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import filters


class CreditApplicationViewSet(viewsets.ModelViewSet):
    queryset = CreditApplication.objects.all()
    serializer_class = CreditApplicationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


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
    # Подключаем фильтры
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # Выбираем поля по которым будем фильтровать
    filter_fields = ("ID", "client_create", "client_update", "client_family", "client_birthday", "client_phone_number",
                     "client_passport_number", "client_scoring_point")
    # Выбираем поля по которым будет производится поиск
    search_fields = ("ID", "client_family")
    # Выираем какие поля можно отсортировать, __all__ значит все поля которые есть в модели
    ordering_fields = "__all__"
    # Поле по которому будет производится сортировка при обращение к API.
    # Думаю логично что партнеров интерисуют клиенты с наибольшим scoring_point
    ordering = ("-client_scoring_point",)


@api_view
def api_root(request, format=None):
    return Response({
        'offers': reverse('offer-list', request=request, format=format),
        'clients': reverse('client-list', request=request, format=format)
    })
