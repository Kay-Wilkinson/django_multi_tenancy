from django.contrib.auth.management.commands import createsuperuser
from django.conf import settings


class Command(createsuperuser.Command):
    def handle(self, *args, **options):
        username = options.get("username")
        password = settings.SUPERUSER_PASSWORD

        try:
            user = self.UserModel.objects.get(username=username)
        except self.UserModel.DoesNotExist:
            self.stdout.write("Creating superuser")
            super(Command, self).handle(*args, **options)
            user = self.UserModel.objects.get(username=username)

        user.set_password(password)
        user.save()