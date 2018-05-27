from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class EquipoSobre_html(TemplateView):
    template_name = "EquipoSobre.html"
