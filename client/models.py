from django.db import models
from tenant_schemas.models import TenantMixin


class ClientTenancy(TenantMixin):
    # TenantMixin will also add model fields: domain_url, schema_name
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
