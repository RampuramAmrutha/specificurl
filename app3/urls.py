from django.urls import path
from app3.views import *

urlpatterns=[
   path('login/',login,name='login'),
   path('table/',table,name='table'),
]