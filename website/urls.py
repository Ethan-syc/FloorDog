from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter/', views.filter_page, name='filter page'),
    path('filter-result/<gender>/<category>', views.filter_result_page, name='filter-result page'),
]