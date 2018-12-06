from django.shortcuts import render, render_to_response

from .forms import *


def index(request):
    return render(request, 'index.html')


def filter_page(request):
    form = MyForm()
    return render_to_response('some_template.html', {'form': form})
