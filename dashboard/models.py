from random import choices
from sre_constants import CATEGORY
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User



CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True)
    category = models.CharField(max_length=20,choices=CATEGORY, null=True,blank=True)
    quantity = models.PositiveIntegerField(null=True,blank=True)

    # class Meta:
    #     verbose_name_plural ='Product'


    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,blank=True)
    staff = models.ForeignKey(User,models.CASCADE,null=True,blank=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'         