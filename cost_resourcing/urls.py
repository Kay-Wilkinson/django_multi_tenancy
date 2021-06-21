from django.urls import path, include
from rest_framework import routers
from cost_resourcing.views import CostResourcingViewSet

router = routers.SimpleRouter()
router.register('', CostResourcingViewSet, basename='cost_resourcing')
urlpatterns = [
    path('', include(router.urls)),
]