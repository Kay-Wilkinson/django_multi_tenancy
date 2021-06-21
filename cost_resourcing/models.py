from django.db import models


class CostResourcingModel(models.Model):
    name = models.TextField()
    description = models.TextField()
    rates = models.TextField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cost_resourcing_model'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
            models.Index(fields=["updated_timestamp"], name="updated_timestamp_idx"),
        ]

