from django.conf.urls import url
from .views import home, fibonacci
urlpatterns = [
    url(r'^$', home),
    url(r'^getvalue/$', fibonacci, name='get_value')
]
