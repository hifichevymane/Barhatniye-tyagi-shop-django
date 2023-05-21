from .models import Product, Category
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404

# Create your views here.

# Главная страница
class HomeView(TemplateView):
    template_name = 'shop/index.html'


# Страница каталога товаров
class ProductsListView(ListView):
    model = Product
    # Переименую object_list на products_list в шаблонах
    context_object_name = 'products_list'


# Products filter by category_slug
class ProductsCategoryListView(ListView):
    template_name = 'shop/products_category_list.html'
    model = Product
    context_object_name = 'products_list'

    # Get products with category = category_slug
    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=category_slug)
        queryset = super().get_queryset().filter(category=category)

        return queryset
    
    # Get context data for html document and add category variable
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        context['category'] = get_object_or_404(Category, slug=category_slug)

        return context


# Страница карточки товара
class CardDetailView(DetailView):
    model = Product


# About page
class AboutTemplateView(TemplateView):
    template_name = 'shop/about.html'
