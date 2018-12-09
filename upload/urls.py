from django.urls import path
from . import views

app_name = 'upload'
urlpatterns = [
    # url(r'^$', 'upload.views.home', name='home'),
    path('', views.home, name='home'),
]