from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Simulacion_html(TemplateView):
    template_name = "simulacion.html"
