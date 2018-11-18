from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from libmgmt.forms import LoginForm, RegisterForm
from django import views
from django.views.generic.edit import FormView
from libmgmt.models import User

# Create your views here.

def auth(request):
    print(request.POST['username'])
    print(request.POST['password'])
    return HttpResponse('Trying to authenticate')

'''def show_home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return HttpResponse('Got all the login data')
    else:
        form = LoginForm()

    return render(request, 'libmgmt/home.html', {
        'form': form
    })'''

'''class LoginView(views.View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'libmgmt/home.html', {
            'form': form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return HttpResponse('Got all the login data')
        return render(request, 'libmgmt/home.html', {
            'form': form
        })'''

class LoginView(FormView):
    template_name = 'libmgmt/home.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        # print(data)
        l = User.objects.filter(**data)
        if len(l):
            return HttpResponse('Valid')
        return HttpResponseRedirect('/lib/home/')

class RegisterView(FormView):
    template_name = 'libmgmt/register.html'
    form_class = RegisterForm
    success_url = '/lib/home/'

    def form_valid(self, form):
        data = form.cleaned_data
        u = User(**data)
        u.save()

        if u.id:
            return super().form_valid(form)
        return HttpResponseRedirect('/lib/register/')

'''def show_register(request):
    # imagine u got the countries from the database
    countries = [
        {
            'code': 'IN',
            'name': 'India'
        },
        {
            'code': 'CR',
            'name': 'Costa Rica'
        },
        {
            'code': 'USA',
            'name': 'United states of america'
        }
    ]

    context = {
        'countries': countries
    }
    return render(request, 'libmgmt/register.html', context)'''
