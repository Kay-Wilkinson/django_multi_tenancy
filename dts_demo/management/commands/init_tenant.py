from django.core.management.base import BaseCommand, CommandError
from client.models import ClientTenancy


class Command(BaseCommand):
    help = 'Creates a first Tenant so we can access our site'

    def handle(self, *args, **kwargs):
        # Do not add port or www here. Change to localhost if running outside of Docker
        tenant = ClientTenancy(domain_url='0.0.0.0',
                               schema_name='tenant1',
                               name='Demo Tenant',
                               )
        try:
            tenant.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created {tenant.name}'))
        except Exception as e:
            raise CommandError(f'{e}: Error encountered whilst initiating {tenant.name}')
