import os
import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.files import *

from .forms import *
from website.models import *
from project316.settings import MEDIA_ROOT


def index(request):
    return render(request, "website/index.html")

# def load_categories(request):
#     filter_form = MyGender(request.POST)
#     if request.method == "POST" and filter_form.is_valid():
#         gender = filter_form.cleaned_data["gender"]
#         if gender == 'M':
#             category = MenClothes.objects.values('category').distinct()
#         else:
#             category = WomenClothes.objects.values('category').distinct()
#         # print(gender)
#         # print(category)
#         return render(request, 'website/filter_page_category_dropdown.html', {'category': category})
#     #     return HttpResponseRedirect(reverse("filter-result page", args=(gender, category)))
#     else:
#         filter_form = MyGender()
#         return render(request, "website/filter_page.html", {"form": filter_form})


def filter_page(request):
    filter_form = FilterForm(request.POST)
    if request.method == "POST" and filter_form.is_valid():
        gender = filter_form.cleaned_data["gender"]
        category = filter_form.cleaned_data["category"]
        # print(gender)
        # print(category)
        return HttpResponseRedirect(
            reverse("filter-result page", args=(gender, category))
        )
    else:
        filter_form = FilterForm()
        return render(request, "website/filter_page.html", {"form": filter_form})


# pagination: ref:https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
def filter_result_page(request, gender, category):
    if gender == "M":
        result_list = MenClothes.objects.filter(category=category)
    else:
        result_list = WomenClothes.objects.filter(category=category)
    paginator = Paginator(result_list, 10)
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
    upload_form = UploadForm(request.POST, request.FILES)
    if request.method == 'POST' and upload_form.is_valid():
        gender = upload_form.cleaned_data["gender"]

        new_file = UploadFile(file=request.FILES['file'])
        new_file.save()

        # current_time = datetime.datetime.now().strftime('%H_%M')
        current_time = "3_14"

        return HttpResponseRedirect(
            reverse("upload-result page", args=(gender, current_time))
        )
    else:
        upload_form = UploadForm()
        return render(request, 'website/upload_page.html', {'form': upload_form})


def upload_result_page(request, gender, current_time):
    current_txt = current_time + '.txt'
    f_path = os.path.join('upload/id_lists/', current_txt)
    with open(f_path, 'r') as f:
        id_list = f.read().split(',')

    if gender == "M":
        result_list = MenClothes.objects.filter(mcid__in=id_list)
    else:
        result_list = WomenClothes.objects.filter(wcid__in=id_list)

    paginator = Paginator(result_list, 10)
    page = request.GET.get("page", 1)
    try:
        paginated_result_list = paginator.page(page)
    except PageNotAnInteger:
        paginated_result_list = paginator.page(1)
    except EmptyPage:
        paginated_result_list = paginator.page(paginator.num_pages)

    return render(
        request,
        "website/upload_result.html",
        {
            "gender": gender,
            "len": len(result_list),
            "result_list": paginated_result_list,
            "paginator": paginator,
        },
    )