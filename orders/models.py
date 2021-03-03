from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
from django.utils.translation import gettext_lazy as _
from shoping.models import Product
from coupons.models import Coupon
from django_jalali.db import models as jmodels

from django.contrib.auth.models import User


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    address = models.CharField(max_length=250, verbose_name="آدرس")
    postal_code = models.CharField(max_length=20, verbose_name="کدپستی")
    city = models.CharField(max_length=100, verbose_name="شهر | استان")
    created = jmodels.jDateField(auto_now_add=True , verbose_name="تاریخ ایجاد")
    updated = jmodels.jDateField(auto_now=True, verbose_name="تاریخ تغییر")
    paid = models.BooleanField(default=False, verbose_name="وضعیت پرداخت")
    coupon = models.ForeignKey(Coupon,
                               related_name='orders',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL, verbose_name="تخفیف")
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])

    
    
    
    
    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * \
            (self.discount / Decimal(100))


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
