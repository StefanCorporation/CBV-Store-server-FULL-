from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = "products/index.html"
    title = 'Establishment-Store'



class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = "products/products.html"
    title = 'Products'
    paginate_by = 3

    def get_queryset(self):
        # контекст формирумем в get_queryset все что связанно с данными из кверисет
        queryset = super(ProductsListView, self).get_queryset()
        # в кваргс у нас хранятся те данные которые передаються в юрл <int:category_id>
        category_id = self.kwargs.get('category_id') 
        return queryset.filter(category_id=category_id) if category_id else queryset


    #контекст мы формируем в   get_context_data 
    def get_context_data(self, **kwargs):
        # в context мы просто создаем словарь как просто в словаре контексt передавали раньше
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
       

        return context
    
         

# basket add functionality ONLY!!!
@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id, request.user)
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# basket delete functionality ONLY!!!
@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])