from django.db import models
from django.urls import reverse
from django.db.models import Q
from django_jalali.db import models as jmodels


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(name__icontains=query)

                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class PriceManager(models.Manager):# اسلایدر اولی سمت چپ
     def get_queryset(self):
       # return super(PriceManager, self).get_queryset().filter(pk__in=[2])
         return super(PriceManager, self).get_queryset().filter(new_category=True).filter(subcategory__id=1)


class AdvansedManager(models.Manager):
     def get_queryset(self):
      
         return super(AdvansedManager, self).get_queryset().filter(new_category=False).filter(subcategory__id=3)



class AdvansedManagerTak(models.Manager):# اولین تصویر سمت راست
     def get_queryset(self):
      
         return super(AdvansedManagerTak, self).get_queryset().filter(new_category=False).filter(subcategory__id=4) # تک جنس







class Category(models.Model):
    name = models.CharField(max_length=200,  db_index=True ,verbose_name="نام- دسته بندی")
    slug = models.SlugField(max_length=200,unique=True)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    objects           = PostManager() 
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'دسته بندی محصولات'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])




class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='souscatégories', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True , verbose_name="نام")
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = jmodels.jDateField(auto_now_add=True , verbose_name="تاریخ ایجاد")
    updated_at = jmodels.jDateField(auto_now=True, verbose_name="تاریخ تغییر")
    
    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'زیر منو'
        verbose_name_plural = 'زیر منوها'
    
    def __str__(self):
        
         return self.name






class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="نام کالا")
    slug = models.SlugField(max_length=200, db_index=True)
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True , verbose_name="تصویر اول")
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True , verbose_name="تصویر دوم")
    description = models.TextField(blank=True, verbose_name='شرح کالا')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت کالا")
    available = models.BooleanField(default=True, verbose_name="موجودی")
    color = models.CharField(max_length=10, null=True, verbose_name="رنگ کالا")
    country =  models.CharField(max_length=30, verbose_name="کشور سازنده")
    created = jmodels.jDateField(auto_now_add=True , verbose_name="تاریخ ایجاد")
    updated = jmodels.jDateField(auto_now=True, verbose_name="تاریخ تغییر")
    new_category = models.BooleanField(default=True, verbose_name="ویژه")
    subcategory = models.ForeignKey(SubCategory, related_name='produits', on_delete=models.CASCADE)
    


    objects = models.Manager() # The default manager.
    objects           = PostManager() 
    lavazemA=  PriceManager()
    advansed_product = AdvansedManager()
    tak_es = AdvansedManagerTak()

    class Meta:
        
        ordering = ('created',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'محصول'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])








