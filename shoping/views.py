from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product, SubCategory
from itertools import chain
from django.http import HttpResponse


from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from django.views.generic import TemplateView

#from.filters import ProductFilter

def product_list(request, category_slug=None, sub_slug=None):
    category = None
    categories = Category.objects.all()
    subs = SubCategory.objects.all()
    products = Product.objects.filter(available=True)
    new_product= Product.lavazemA.all()
    advansed_pro =Product.advansed_product.all()
    taki= Product.tak_es.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    if sub_slug:
        subs = get_objects_or_404(SubCategory, slug=sub_slug)
        products = products.filter(subcategory=subs)
       
       
       
    return render(request,
                  'shop/product/just.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,'subs':subs,'new_product':new_product, 'advansed':advansed_pro,'taki':taki})





def product_detail(request, id, slug):
   
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product/page-single.html',
                  {'product': product,"cart_product_form":cart_product_form})



class SearchView(ListView):
    template_name = "view.html"
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            blog_results = Product.objects.search(query)
            #lesson_results = Product.objects.search(query)
            #profile_results = Service.objects.search(query)

            # combine querysets 
            queryset_chain = chain(
                blog_results,
                #lesson_results,
                #profile_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Product.objects.none()  # just an empty queryset as default
        

# filter product 

# def filter_product(request):
#      f = ProductFilter(request.GET, queryset=Product.objects.all())
#      return render(request, "shop/product/filter_1.html", {"filter":f})

       
       
       
        
        
class MyShopOrder(TemplateView):
    template_name ="shop/product/order.html"
        
        
        
        