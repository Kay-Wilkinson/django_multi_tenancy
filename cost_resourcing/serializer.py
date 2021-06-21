from rest_framework import serializers

from cost_resourcing.models import CostResourcingModel


class CostResourcingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostResourcingModel
        fields = ('name', 'description', 'rates', 'created_timestamp', 'updated_timestamp')