from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def activate(request):
    return  HttpResponse('please activate my account')
def run(request):
    return render(request,'run.html')