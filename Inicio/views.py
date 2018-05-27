from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def index_html(request):
#         return render(request, 'index.html', {})

class index_html(TemplateView):
    template_name = "index.html"
