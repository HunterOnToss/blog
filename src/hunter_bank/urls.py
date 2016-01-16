from hunter_bank.views import OfferViewSet
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


router = DefaultRouter()
router.register(r'offers', views.OfferViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

