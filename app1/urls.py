from django.urls import path
from app1.views import *

urlpatterns=[
    path('activate/',activate,name='activate'),
    path('run/',run,name='run'),
] 