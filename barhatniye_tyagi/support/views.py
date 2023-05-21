from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView
from .models import Message
from .forms import SupportForm

# Create your views here.
class HelpCreateView(CreateView):
    form_class = SupportForm
    model = Message
    success_url = reverse_lazy('support:thank_you')


class HelpView(FormView):
    form_class = SupportForm
    template_name = 'support/help_form.html'

    success_url = reverse_lazy('support:thank_you')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'support/thank-you.html'
