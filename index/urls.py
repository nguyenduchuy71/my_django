from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

CACHE_TIME = 5*60

urlpatterns = [
    path('', cache_page(CACHE_TIME)(views.IndexView.as_view()), name='index'),
]
