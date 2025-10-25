from django.shortcuts import render

from hunger import forms
from hunger.models import Dish, Shopcart
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class DishView(ListView):
    model = Dish
    template_name = 'main_page.html'
    context_object_name = 'dishes'


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish_view.html'
    context_object_name = 'dish'

class  ShopcartView(LoginRequiredMixin, ListView):
    model = Shopcart
    template_name = 'shopcart.html'
    context_object_name = 'shopcarts'
    
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
    

class ShopcartCreateView(LoginRequiredMixin, CreateView):
    model = Shopcart
    form_class = forms.ShopcartForm
    template_name = 'shopcart_create.html'
    success_url = reverse_lazy('shopcart')
    
    def get_queryset(self):
        return Shopcart.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
    #похуй я полагодив

    
    
class ShopcartUpdateView(LoginRequiredMixin, UpdateView):
    model = Shopcart
    form_class = forms.ShopcartUpdateForm
    template_name = 'shopcart_update.html'
    success_url = reverse_lazy('shopcart')

    def get_queryset(self):
        return Shopcart.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
    


class ShopcartDeleteView(LoginRequiredMixin, DeleteView):
    model = Shopcart
    template_name = 'shopcart_delete.html'
    success_url = reverse_lazy('shopcart')


