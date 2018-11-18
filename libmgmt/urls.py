from django.urls import path

from libmgmt import views
# lib/

app_name = 'library'

urlpatterns = [
    path('home/', views.LoginView.as_view(), name='showhome'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('authenticate/', views.auth, name='auth')
]
