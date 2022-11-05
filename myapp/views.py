from django.shortcuts import render
from .models import *

def talks(request):
  talks = Talk.objects.order_by('title')
  context = {'talks': talks}
  return render(request, 'myapp/talks.html', context)