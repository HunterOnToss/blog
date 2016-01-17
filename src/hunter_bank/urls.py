from hunter_bank.views import OfferViewSet, ClientViewSet
from hunter_bank import views

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


offer_list = OfferViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

offer_detail = OfferViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

client_list = ClientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

client_detail = ClientViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = DefaultRouter()
router.register(r'offers', views.OfferViewSet)
router.register(r'clients', views.ClientViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

