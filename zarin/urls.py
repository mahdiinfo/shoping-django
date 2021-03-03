from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

# from .views import Home
# from payment.views import send_request, verify

from django.contrib import admin
admin.site.site_header = 'لوازم پزشکی امیر'
admin.site.site_title = 'لوازم پزشکی زرین طب باستان'

urlpatterns = [
    path('amir/', admin.site.urls),
   
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('shoping.urls', namespace='shop')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    #path('zarin/request/', send_request, name='request'),
    #path('zarin/verify/', verify , name='verify'),



]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)