from django.urls import path
from rest_framework import routers
from . import views



urlpatterns = [

    path('', views.index, name='index'),

    path('login', views.login , name='login'),

    path('createAccount', views.createAccount , name='createAccount')

    #path('dashboard', views.dashboard , name='dashboard')

]


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

