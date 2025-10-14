from django.urls import path
from chef.views import home

urlpatterns = [
    path('', home.as_view(),name='home'),
]