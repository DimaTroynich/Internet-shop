from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, request, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from cart.forms import CartAddProductForm
from .models import Category, Catalog, Product


def category_list(request):
    category = Category.objects.all()
    context = {'category': category
    }
    return render(request, 'store/category_list.html', context=context)


def catalog_list(request, id):
    category = get_object_or_404(Category, id=id)
    catalog = Catalog.objects.filter(category_id=id)
    context = {'category': category, 'catalog': catalog
               }
    return render(request, 'store/catalog_list.html', context=context)

def product_list(request, id):
    catalog = get_object_or_404(Catalog, id=id)
    product = Product.objects.filter(catalog_id=id)
    context = {'catalog': catalog, 'product': product
               }
    return render(request, 'store/product_list.html', context=context)



# class ProductListView(ListView):
#     model = Product
#     template_name = 'product_list.html'
#     context_object_name = "product"


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)

    cart_product_form = CartAddProductForm()
    return render(request, 'store/product_detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})





