from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

# Name App
app_name = 'store'

# Paths to templates with app store views
urlpatterns = [
    path('', category_list, name='category-list'),
    path('catalog/<int:id>/', catalog_list, name='catalog-list'),
    path('product/<int:id>', product_list, name='product-list'),
    path('catalog/product/<int:pk>', product_detail, name='product-detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



