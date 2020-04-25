from dj_static import Cling
from django.core.wsgi import get_wsgi_application
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_database.settings')

application = Cling(get_wsgi_application())
