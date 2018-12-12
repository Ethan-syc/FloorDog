from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("filter/", views.filter_page, name="filter page"),
    path('upload/', views.upload_page, name='upload page'),

    path(
        "filter-result/<gender>/<category>/<material>/<design>",
        views.filter_result_page,
        name="filter-result page",
    ),

    path(
        "clothes-detail/<gender>/<int:pk>",
        views.clothes_detail,
        name="clothes-detail page",
    ),

    path(
        'upload-gender/',
        views.upload_gender_page,
        name='upload-gender page'
    ),

    path(
        "upload-result/<gender>",
        views.upload_result_page,
        name="upload-result page",
    ),
]
