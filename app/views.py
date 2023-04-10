from django.shortcuts import render
from django.views.generic import TemplateView

class empl(TemplateView):
    template_name = 'home.html'


class qaz(TemplateView):
    template_name='about.html'


# Create your views here.
