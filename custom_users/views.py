from django.shortcuts import render
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/login'

class InloginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('persons:persons_list')

class OutLogoutView(LogoutView):
    next_page = reverse_lazy('persons:login')
    

class UserListView(ListView):
    template_name = 'registration/user_list.html'
    model = User
    context_object_name = 'user'

    def get_queryset(self):
        return User.objects.all()