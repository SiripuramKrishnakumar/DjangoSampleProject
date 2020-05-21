from django.urls import path
from .serializers import *
from django.conf.urls import url
from .api import CustomerDetails, CreateCustomer,UpdateCustomer
from .AuthenticationApi import *

urlpatterns = [
    url(r'^api/getAllCustomers/$', CustomerDetails.as_view(), name="customersList"),
    url(r'^api/CreateCustomers/(?P<customerId>\d+)/$', CreateCustomer.as_view(), name="customer"),
    url(r'^api/UpdateCustomer/(?P<customerId>\d+)/$', UpdateCustomer.as_view(),name='update_customer')
]

urlpatterns += [
    url(r'^api/auth/$', CustomAuthToken.as_view(), name='auth')
]