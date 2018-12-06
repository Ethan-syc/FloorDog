from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import *


def index(request):
    return render(request, 'index.html')


# form = MyForm()
# return render_to_response('some_template.html', {'form': form})

def filter_page(request):
    filter_form = MyForm(request.POST)
    if request.method == 'POST' and filter_form.is_valid():
        gender = filter_form.cleaned_data['gender']
        category = filter_form.cleaned_data['category']
        print(gender)
        print(category)
        # if gender == 'M':
        #         #     men_result_list =
        #         # else:
        #         #     pass
        return HttpResponseRedirect(reverse('filter page', args=()))
    else:
        filter_form = MyForm()
        return render(request, 'some_template.html', {'form': filter_form})
