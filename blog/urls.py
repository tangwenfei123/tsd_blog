from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.login, name='login'),
    path('', views.loginout, name='logout'),
]


