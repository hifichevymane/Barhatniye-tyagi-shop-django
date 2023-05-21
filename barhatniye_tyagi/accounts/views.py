from .forms import RegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import FormView, TemplateView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Registration page
class RegisterView(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('shop:home')
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()

        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']

        user = authenticate(email=email, password=password)
        if user is not None and user.is_active:
            login(self.request, user)

        return super(RegisterView, self).form_valid(form)


# Login view
# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     form_class = LoginForm
#     success_url = reverse_lazy('shop:home')
#     authentication_form = LoginForm
#     username_field = None


# Login view
class CustomLoginView(FormView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('shop:home')

    # Validating form
    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Неправильный пароль или почта')
            return self.form_invalid(form)


# Account page
class CabinetView(TemplateView):
    template_name = 'accounts/cabinet.html'
