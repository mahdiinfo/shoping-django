from django.db import models
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
from jalali_date import datetime2jalali, date2jalali # new

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True ,verbose_name="کوپن تخفیف")
    valid_from = models.DateTimeField(verbose_name="تاریخ شروع")
    valid_to = models.DateTimeField(verbose_name= "انقضاء")
    discount = models.IntegerField(
                   validators=[MinValueValidator(0),
                               MaxValueValidator(100)] ,verbose_name="تخفیف")
    active = models.BooleanField()

    class Meta:
        verbose_name_plural = "تنظیمات طرح تخفیف"

    def __str__(self):
        return self.code

    
