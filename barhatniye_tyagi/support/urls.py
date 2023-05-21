from django.urls import path
from . import views

app_name='support'

urlpatterns = [
    path('', views.HelpCreateView.as_view(), name='help'),
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you')
]
