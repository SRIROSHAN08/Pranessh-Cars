from django.urls import path
from .views import *

urlpatterns = [
    path('',AllCarsView.as_view(),name='homepage'),
    path('car/<int:pk>',CarDetailView.as_view(),name='car-detail'),
    path('contact/',ContactView,name='contact')
]