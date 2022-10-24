from django.shortcuts import render
from .models import Page
# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def history(request):
    return render(request, 'core/history.html')

def other(request, page_id):
    page = Page.objects.get(id = page_id)
    return render(request, 'core/other.html',{'page':page})

def visit(request):
    return render(request, 'core/visit.html')