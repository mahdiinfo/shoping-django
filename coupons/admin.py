from django.contrib import admin
import json
from.models import Coupon


from packaging import version
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django_jalali.admin.filters import JDateFieldListFilter
from.models import Coupon
import django_jalali.admin as jadmin

import django
from django.conf import settings
from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
from django.contrib.postgres.fields.jsonb import JSONField

from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	




class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
	model = Coupon

class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
	model = Coupon



@admin.register(Coupon)
class CouponAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to',
                    'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']
