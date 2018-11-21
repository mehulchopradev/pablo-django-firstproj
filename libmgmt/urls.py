from django.urls import path

from libmgmt import views
# lib/

app_name = 'library'

urlpatterns = [
    path('home/', views.LoginView.as_view(), name='showhome'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('authenticate/', views.auth, name='auth'),
    path('private-home/', views.show_private_home, name='privatehome'),
    path('book-details/<int:book_id>', views.show_book, name='bookdetails')
]
