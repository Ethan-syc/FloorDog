# import os
# import datetime
# import subprocess

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import *
from website.models import *
# from . import recommend


def index(request):
    return render(request, "website/index.html")


def filter_page(request):
    gender_form = GenderForm(request.POST)
    filter_form = FilterForm(request.POST)
    material_form = MaterialForm(request.POST)
    design_form = DesignForm(request.POST)

    if request.method == "POST" and filter_form.is_valid() \
            and gender_form.is_valid() and material_form.is_valid() and design_form.is_valid():

        gender = gender_form.cleaned_data["gender"]
        category = filter_form.cleaned_data["category"]
        material = material_form.cleaned_data["material"]
        design = design_form.cleaned_data["design"]

        return HttpResponseRedirect(
            reverse("filter-result page", args=(gender, category, material, design))
        )

    else:
        gender_form = GenderForm()
        filter_form = FilterForm()
        material_form = MaterialForm()
        design_form = DesignForm()
        return render(request, "website/filter_page.html",
                      {"gender_form": gender_form, "filter_form": filter_form,
                       "material_form": material_form, "design_form": design_form})


# pagination: ref:https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
def filter_result_page(request, gender, category, material, design):
    result_list = []

    if gender == "M" and material == "All" and category == "All" and design == "All":
        result_list = MenClothes.objects.all()
    if gender == "W" and material == "All" and category == "All" and design == "All":
        result_list = WomenClothes.objects.all()

    if gender == "M" and material == "All" and category != "All" and design == "All":
        result_list = MenClothes.objects.filter(category__icontains=category)
    if gender == "W" and material == "All" and category != "All" and design == "All":
        result_list = WomenClothes.objects.filter(category__icontains=category)

    if gender == "M" and category == "All" and material != "All" and design == "All":
        result_list = MenClothes.objects.filter(material__icontains=material)
    if gender == "W" and category == "All" and material != "All" and design == "All":
        result_list = WomenClothes.objects.filter(material__icontains=material)

    if gender == "M" and category == "All" and material == "All" and design != "All":
        result_list = MenClothes.objects.filter(clothes_detail__icontains=design)
    if gender == "W" and category == "All" and material == "All" and design != "All":
        result_list = WomenClothes.objects.filter(clothes_detail__icontains=design)

    if gender == "M" and category != "All" and material != "All" and design == "All":
        result_list = MenClothes.objects.filter(category__icontains=category).filter(material__icontains=material)
    if gender == "W" and category != "All" and material != "All" and design == "All":
        result_list = WomenClothes.objects.filter(category__icontains=category).filter(material__icontains=material)

    if gender == "M" and category == "All" and material != "All" and design != "All":
        result_list = MenClothes.objects.filter(clothes_detail__icontains=design).filter(material__icontains=material)
    if gender == "W" and category == "All" and material != "All" and design != "All":
        result_list = WomenClothes.objects.filter(clothes_detail__icontains=design).filter(material__icontains=material)

    if gender == "M" and category != "All" and material == "All" and design != "All":
        result_list = MenClothes.objects.filter(clothes_detail__icontains=design).filter(category__icontains=category)
    if gender == "W" and category != "All" and material == "All" and design != "All":
        result_list = WomenClothes.objects.filter(clothes_detail__icontains=design).filter(category__icontains=category)

    if gender == "M" and category != "All" and material != "All" and design != "All":
        result_list = MenClothes.objects.filter(clothes_detail__icontains=design).filter(category__icontains=category).filter(material__icontains=material)
    if gender == "W" and category != "All" and material != "All" and design != "All":
        result_list = WomenClothes.objects.filter(clothes_detail__icontains=design).filter(category__icontains=category).filter(material__icontains=material)

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
    # gender_form = GenderForm(request.POST, prefix='gender')
    upload_form = UploadForm(request.POST, request.FILES)

    if request.method == 'POST' and upload_form.is_valid():
        # gender = upload_form.cleaned_data["gender"]
        new_file = UploadFile(file=request.FILES['file'])
        new_file.save()

        # current_time = datetime.datetime.now().strftime('%H_%M')
        # current_time = "3_14"

        # subprocess.run("upload/recommend.py")
        # subprocess.check_call(["python3.7", "/upload/recommend.py"])
        # recommend()

        return HttpResponseRedirect(
            reverse("upload-gender page")
        )
    else:
        upload_form = UploadForm()
        # gender_form = GenderForm(prefix='gender')
        return render(request, 'website/upload_page.html', {'upload_form': upload_form})


def upload_gender_page(request):
    gender_form = GenderForm(request.POST)
    if request.method == 'POST' and gender_form.is_valid():
        gender = gender_form.cleaned_data["gender"]
        return HttpResponseRedirect(
            reverse("upload-result page", args=gender)
        )
    else:
        gender_form = GenderForm()
        return render(request, 'website/upload_gender.html', {'gender_form': gender_form})


def upload_result_page(request, gender):
    # current_txt = current_time + '.txt'
    f_path = 'upload/id_lists/result.txt'
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