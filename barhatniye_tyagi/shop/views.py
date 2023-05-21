from .models import Product
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

# Главная страница
class HomeView(TemplateView):
    template_name = 'shop/index.html'


# Страница каталога товаров
class ProductsListView(ListView):
    model = Product
    # Переименую object_list на products_list в шаблонах
    context_object_name = 'products_list'


class ProductsCategoryListView(ListView):
    template_name = 'shop/products_category_list.html'
    model = Product
    context_object_name = 'products_list'


# Страница карточки товара
class CardDetailView(DetailView):
    model = Product


# About page
class AboutTemplateView(TemplateView):
    template_name = 'shop/about.html'
