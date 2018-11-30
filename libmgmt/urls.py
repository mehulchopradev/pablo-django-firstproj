from django.urls import path
from django.views.generic import TemplateView

from libmgmt import views
# lib/

app_name = 'library'

urlpatterns = [
    path('home/', views.LoginView.as_view(), name='showhome'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('authenticate/', views.auth, name='auth'),
    path('private-home/', views.show_private_home, name='privatehome'),
    path('book-details/<int:book_id>', views.show_book, name='bookdetails'),
    path('logout/', views.logout, name='logout'),
    path('issue-book/<int:book_id>', views.issue_book, name='issue'),
    path('return-book/<int:book_id>', views.return_book, name='return'),
    path('create-book/', views.BookCreateView.as_view()),
    path('book-list/', views.BookList.as_view(), name='booklist'),
    path('about-us/', TemplateView.as_view(template_name='libmgmt/about-us.html')),
    path('books/<int:pk>', views.BookUpdateView.as_view())
]
