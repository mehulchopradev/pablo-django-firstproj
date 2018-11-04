from django.shortcuts import render

# Create your views here.

def show_home(request):
    return render(request, 'libmgmt/home.html')

def show_register(request):
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
    return render(request, 'libmgmt/register.html', context)
