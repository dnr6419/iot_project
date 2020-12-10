from django.urls import path
from .views import *

urlpatterns = [
    path('',MainTV.as_view()),
    path('upload',FileUploadFV.as_view()),
    path('scan',FileUploadFV.as_view()),
]