from django.shortcuts import render, redirect
from django.http.response import JsonResponse 
from django.views.generic.base import TemplateView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from casinoaffiliate_app.models import Casino, Bonus, AdminReview, GameAccount

class IndexView(TemplateView):
    template_name = 'casinoaffiliate_app/index.html'

    def get(self,request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['casinos'] = Casino.objects.all().order_by('-id')
        return render(request, self.template_name, context)

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

class GameView(TemplateView):
    template_name = 'casinoaffiliate_app/game.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        acc = GameAccount.objects.filter(user=request.user.id)

        context['balance'] = int(acc.first().balance) if acc else 0
        return render(request, self.template_name, context)

class ProfileView(TemplateView):
    template_name = 'casinoaffiliate_app/profile.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        acc = GameAccount.objects.filter(user=request.user.id)

        context['balance'] = int(acc.first().balance) if acc else 0
        return render(request, self.template_name, context)

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

@login_required
def get_balance(request):
    acc = GameAccount.objects.get(user=request.user)
    return JsonResponse({'value': acc.balance, 'status': 'OK'})

@login_required
def update_balance(request):
    if request.GET:
        return JsonResponse({}, status=400)

    acc = GameAccount.objects.get(user=request.user)
    acc.balance = request.POST.get('bet')
    acc.save()
    return JsonResponse({'value': acc.balance, 'status': 'OK'})