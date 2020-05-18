from django.urls import path
from .serializers import *
from django.conf.urls import url
from .api import CustomerDetails


urlpatterns = [
    url(r'^api/getallcustomers/$', CustomerDetails.as_view(), name="customersList")
]