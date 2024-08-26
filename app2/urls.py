from django.urls import path
from app2.views import *

urlpatterns=[
    path('act/',act,name='act'),
    path('stuckked/',stuckked,name='stuckked'),
]