from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import generics

# Create your views here.
def home(request):
  return render(request, 'index.html')

class MenuView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer