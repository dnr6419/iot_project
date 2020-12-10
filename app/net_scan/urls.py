from django.urls import path
from .views import *

urlpatterns = [
    path('',MainTV.as_view()),
    path('results', listLV.as_view()),
    path('settings', setLV.as_view()),
]