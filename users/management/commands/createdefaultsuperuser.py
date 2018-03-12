from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from users.models import User

class Command(BaseCommand):
    help = 'Create default superuser account'
    
    # change the username and password to your admin.
    def handle(self, **options):
        try:
            user = User.objects.create_superuser(username='your_admin_account', email=None, password='your_admin_password')
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created."))
        except IntegrityError:
            self.stdout.write(self.style.NOTICE("Superuser 'admin' already exists."))
