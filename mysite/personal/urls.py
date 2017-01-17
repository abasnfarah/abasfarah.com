from django.conf.url import url, include
from . import views

urlpatterns = [
        url('r^$', views.index, name="index"),
        ]
