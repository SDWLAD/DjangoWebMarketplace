from django.urls import path

from .views import *

urlpatterns = [
    path("", IndexView.as_view()),
    path('<int:pk>', ItemDetailView.as_view()),
    path("about/", about_view)
]