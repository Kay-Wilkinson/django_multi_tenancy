from rest_framework import viewsets
from cost_resourcing.models import CostResourcingModel


class CostResourcingViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return CostResourcingModel.objects.all()

    serializer_class = CostResourcingModel
