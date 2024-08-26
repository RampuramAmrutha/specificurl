from django.shortcuts import render

# Create your views here.
def act(request):
    return render(request,'act.html')
def stuckked(request):
    return render(request,'stuckked.html')