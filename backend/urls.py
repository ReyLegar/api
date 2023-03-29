from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import CustomerList
from django.contrib import admin

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('admin/', admin.site.urls),
]
