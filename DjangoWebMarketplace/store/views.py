from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MarketplaceItem

class IndexView(ListView):
    model = MarketplaceItem
    template_name = "store/index.html"