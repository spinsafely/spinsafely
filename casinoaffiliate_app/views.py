from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe
from casinoaffiliate_app.models import Casino, Bonus, AdminReview

class IndexView(TemplateView):
    template_name = 'casinoaffiliate_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['casinos'] = Casino.objects.all()

        return context

class CasinoView(TemplateView):
    template_name = 'casinoaffiliate_app/casino.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['casino'] = Casino.objects.get(slug=kwargs['slug'])
        context['pros'] = Casino.objects.get(slug=kwargs['slug']).pros.split('\n')
        context['cons'] = Casino.objects.get(slug=kwargs['slug']).cons.split('\n')
        context['casinos'] = Casino.objects.all()
        return context

class RegisterView(TemplateView):
    template_name = 'casinoaffiliate_app/register.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'casinoaffiliate_app/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')
