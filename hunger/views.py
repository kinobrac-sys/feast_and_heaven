from django.shortcuts import render

from hunger import forms
from hunger.models import Dish, Shopcart
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class DishView(ListView):
    model = Dish
    template_name = 'main_page.html'
    context_object_name = 'dishes'


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish_detail.html'
    context_object_name = 'dish'

class  ShopcartView(LoginRequiredMixin, ListView):
    model = Shopcart
    template_name = 'shopcart.html'
    context_object_name = 'shopcart'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.ShopcartForm()
        return context

    def get_queryset(self):
        queryset = Shopcart.objects.filter(user=self.request.user)
        category = self.request.GET.get('category')

        if category:
            queryset = queryset.filter(item__category=category)

        return queryset
            

class ShopCartAddView(DetailView):
    model = Shopcart
    template_name = 'shopcart_add.html'
    context_object_name = 'shopcart_add'