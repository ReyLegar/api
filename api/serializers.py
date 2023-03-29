from rest_framework import serializers
from api.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'patronymic', 'payment_arrears']
