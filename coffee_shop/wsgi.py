import os
import environ


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coffee_shop.settings")
# os.environ['DJANGO_SETTINGS_MODULE'] = 'coffee_shop.settings'

application = get_wsgi_application()
