from django.urls import path

from libmgmt import views
# lib/

app_name = 'library'

urlpatterns = [
    path('home/', views.show_home),
    path('register/', views.show_register, name='register')
]
