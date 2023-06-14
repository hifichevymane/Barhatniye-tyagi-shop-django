from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('products/<slug:category_slug>', views.ProductsCategoryListView.as_view(), name='products-category'),
    path('products/card/<slug:slug>', views.CardDetailView.as_view(), name='card'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
]
