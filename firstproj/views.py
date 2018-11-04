from django.http import HttpResponse # to send anything back to the client
from django.shortcuts import render
from datetime import datetime

def show_home(request):
    # request -> Django request object (whenever we want to get anything from the client)
    # return HttpResponse('<html><body><h2>Welcome to my home page</h2></body></html>')
    dt = datetime.now()
    hour = dt.hour
    if hour >= 0 and hour < 12:
        message = 'Good Morning'
    elif hour >= 12 and hour < 16:
        message = 'Good Afternoon'
    else:
        message = 'Good Evening'

    # data to be passsed to the django template
    context = {
        'greeting_message': message
    }

    return render(request, 'home.html', context)

def show_contactus(request):
    # ur email and mobile is coming from the databases
    email = 'pablo@gmail.com'
    mobile = '98345349534'
    addresses = [
        {
            'country': 'India',
            'tel': '2454646456'
        },
        {
            'country': 'Costa Rica',
            'tel': '56756546'
        },
        {
            'country': 'USA',
            'tel': '932649334'
        }
    ]
    context = {
        'email': email,
        'mobile': mobile,
        'addresses': addresses
    }
    return render(request, 'contactus.html', context)
