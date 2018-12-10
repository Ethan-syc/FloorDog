from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("filter/", views.filter_page, name="filter page"),
    path('upload/', views.upload_page, name='upload page'),

    # path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),

    path(
        "filter-result/<gender>/<category>",
        views.filter_result_page,
        name="filter-result page",
    ),

    path(
        "clothes-detail/<gender>/<int:pk>",
        views.clothes_detail,
        name="clothes-detail page",
    ),

    path(
        "upload_result/<gender>/<current_time>",
        views.upload_result_page,
        name="upload-result page",
    ),
]
