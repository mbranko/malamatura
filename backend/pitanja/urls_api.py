from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pitanja.views_api import *

app_name = 'pitanja'

urlpatterns = [
    path('testovi/', TestList.as_view()),
    path('testovi/<int:pk>/', TestDetail.as_view()),
    path('pitanja/', PitanjeList.as_view()),
    path('pitanja/<int:pk>/', PitanjeDetail.as_view()),
    path('odgovori/', OdgovorList.as_view()),
    path('odgovori/<int:pk>/', OdgovorDetail.as_view()),
    path('komplet-test/<int:pk>/', KompletTestDetail.as_view()),
    path('komplet-pitanje/<int:pk>/', KompletPitanjeDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
