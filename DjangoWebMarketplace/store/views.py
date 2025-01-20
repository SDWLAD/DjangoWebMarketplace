from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MarketplaceItem

class IndexView(ListView):
    model = MarketplaceItem
    template_name = "store/index.html"
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = MarketplaceItem.objects.values('category').distinct()
        return context