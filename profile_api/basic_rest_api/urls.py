from django.urls import path
from basic_rest_api import views
urlpatterns = [
    path('', views.index)
]