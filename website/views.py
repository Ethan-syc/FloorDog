from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import *
from .models import *


def index(request):
    return render(request, "website/index.html")


def filter_page(request):
    filter_form = MyForm(request.POST)
    if request.method == "POST" and filter_form.is_valid():
        gender = filter_form.cleaned_data["gender"]
        category = filter_form.cleaned_data["category"]
        # print(gender)
        # print(category)
        return HttpResponseRedirect(
            reverse("filter-result page", args=(gender, category))
        )
    else:
        filter_form = MyForm()
        return render(request, "website/filter_page.html", {"form": filter_form})


# pagination: ref:https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
def filter_result_page(request, gender, category):
    # print(gender)
    # print(category)
    if gender == "M":
        result_list = MenClothes.objects.filter(category=category)
    else:
        result_list = WomenClothes.objects.filter(category=category)
    paginator = Paginator(result_list, 12)
    page = request.GET.get("page", 1)
    try:
        paginated_result_list = paginator.page(page)
    except PageNotAnInteger:
        paginated_result_list = paginator.page(1)
    except EmptyPage:
        paginated_result_list = paginator.page(paginator.num_pages)
    return render(
        request,
        "website/filter_result.html",
        {
            "gender": gender,
            "category": category,
            "len": len(result_list),
            "result_list": paginated_result_list,
            "paginator": paginator,
        },
    )


def clothes_detail(request, gender, pk):
    if gender == "M":
        clothes = get_object_or_404(MenClothes, pk=pk)
    else:
        clothes = get_object_or_404(WomenClothes, pk=pk)
    return render(request, "website/detail_page.html", {"clothes": clothes})


def upload_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file=request.FILES['file'])
            new_file.save()

            return HttpResponseRedirect(reverse('upload:home'))
    else:
        form = UploadFileForm()

    data = {'form': form}
    return render(request, 'website/upload_page.html', data)
