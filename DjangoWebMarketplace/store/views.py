from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MarketplaceItem
from django.views.generic.detail import DetailView

class IndexView(ListView):
    model = MarketplaceItem
    template_name = "store/index.html"
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = MarketplaceItem.objects.values('category').distinct()
        return context

class ItemDetailView(DetailView):
    model = MarketplaceItem
    template_name = "store/item_detail.html"
    context_object_name = 'item'


def about_view(request):
    return render(request, 'store/about.html')