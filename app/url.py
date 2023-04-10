from django.urls import path
from .views import empl, qaz

urlpatterns = [
    path('about/',qaz.as_view(),name='about'), 
    path('', empl.as_view(), name='home')
]