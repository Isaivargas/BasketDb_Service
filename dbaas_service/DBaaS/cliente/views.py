

# Create your views here.
from rest_framework import viewsets
from .import serializers
from .serializers import ClienteSerializer
from .models import Cliente

from django.template.loaders.base import Loader
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
   template = get_template('index.html') # getting our template	 
   return HttpResponse(template.render())

def login(request):
   template = get_template('login.html') # getting our template	 
   return HttpResponse(template.render())

def createAccount(request):
   template = get_template('create-account.html') # getting our template	 
   return HttpResponse(template.render())




class ClienteView(viewsets.ModelViewSet):
      serializer_class = ClienteSerializer
      queryset = Cliente.objects.all()




