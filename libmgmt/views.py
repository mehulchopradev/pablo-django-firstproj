from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from libmgmt.forms import LoginForm, RegisterForm
from django import views
from django.views.generic.edit import FormView
from libmgmt.models import User
from libmgmt.models import Book

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
            # the user authentication succeeded
            u = l[0]
            self.request.session['userid'] = u.id
            self.request.session['username'] = u.username

            # remember the id and username in a session
            # session is stored in the server memory
            # session is user browser specific
            # 1 session object per user browser logged in
            return HttpResponseRedirect(reverse('library:privatehome'))
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

def show_private_home(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('library:showhome'))
    # retrieve the session (automatically retrieved for the request coming from that specific browser)
    # retrieved the stored data from the session
    username = request.session['username']
    userid = request.session['userid']

    blist = Book.objects.order_by('price')
    for book in blist:
        users = book.user_set.all()
        book.cannotissue = False

        if book.count == len(users):
            book.cannotissue = True
        else:
            fusers = [user for user in users if user.id == userid]
            if len(fusers):
                book.notissued = False # derived property added in the model
            else:
                book.notissued = True # derived property added in the model
    context = {
        'booklist': blist,
        'username': username
    }

    return render(request, 'libmgmt/privatehome.html', context)

def show_book(request, book_id):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('library:showhome'))

    # I need to get the id of the book (From the request), whose details I want to fetch from the database
    book = Book.objects.get(pk=book_id)
    username = request.session['username']
    context = {
        'book': book,
        'username': username
    }

    return render(request, 'libmgmt/book.html', context)

def issue_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = User.objects.get(pk=request.session['userid'])

    user.books_issued.add(book)

    return HttpResponseRedirect(reverse('library:privatehome'))

def return_book(request, book_id):
    user = User.objects.get(pk=request.session['userid'])
    user.books_issued.remove(book_id)

    return HttpResponseRedirect(reverse('library:privatehome'))

def logout(request):
    request.session.flush();

    return HttpResponseRedirect(reverse('library:showhome'))

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
