from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def app6_dc(request):
    return HttpResponse('delhi capitals')