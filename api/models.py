from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    payment_arrears = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'
