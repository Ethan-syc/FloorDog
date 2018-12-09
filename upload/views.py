from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from django.shortcuts import render

from upload.forms import UploadFileForm
from upload.models import UploadFile


def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file=request.FILES['file'])
            new_file.save()

            return HttpResponseRedirect(reverse('upload:home'))
    else:
        form = UploadFileForm()

    data = {'form': form}
    return render(request, 'upload/index.html', data)