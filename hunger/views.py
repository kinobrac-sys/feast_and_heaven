from django.shortcuts import render

from hunger import forms
from hunger.models import Dish, Order, Shopcart, OrderItem, Order
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
    login_url = reverse_lazy('login-page')

    def post(self, request, *args, **kwargs):
        login_url = reverse_lazy('login-page')
        dish = self.get_object()
        shopcart = Shopcart.objects.filter(item=dish, user=request.user).first()
        if shopcart:
            shopcart.quantity += 1
            shopcart.save()
        else:
            Shopcart.objects.create(item=dish, user=request.user, quantity=1)
        return render(request, 'dish_view.html', {'dish': dish, 'message': 'Додано до кошика!'})
    
class  ShopcartView(LoginRequiredMixin, ListView):
    model = Shopcart
    template_name = 'shopcart.html'
    context_object_name = 'shopcarts'
    login_url = reverse_lazy('login-page')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.ShopcartForm()
        shopcarts = self.get_queryset()
        total_price = sum([shopcart.get_total_price() for shopcart in shopcarts])
        context['total_price'] = total_price
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
    login_url = reverse_lazy('login-page')
    
    def get_queryset(self):
        return Shopcart.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    
    
class ShopcartUpdateView(LoginRequiredMixin, UpdateView):
    model = Shopcart
    form_class = forms.ShopcartUpdateForm
    template_name = 'shopcart_update.html'
    success_url = reverse_lazy('shopcart')
    login_url = reverse_lazy('login-page')

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

class PayView(ListView):
    template_name = 'tomfoolery.html'
    
    def get(self, request):
        return render(request, 'tomfoolery.html')


'''def create_order(request):
    shopcarts = Shopcart.objects.filter(user=request.user)
    for cart in shopcarts:
        Order.objects.create(carter=cart, user=request.user)
    #shopcarts.delete()
    return render(request, 'order_created.html')'''


class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = forms.OrderForm
    template_name = 'order.html'
    context_object_name = 'orders'
    login_url = reverse_lazy('login-page')
    success_url = reverse_lazy('view_order')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        order = form.save()
        shopcarts = Shopcart.objects.filter(user=user)
        for cart in shopcarts:
            OrderItem.objects.create(
                order=order,
                dish=cart.item,
                quantity=cart.quantity
            )
        return super().form_valid(form)
    
    
    


    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class ViewOrder(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'view_order.html'
    context_object_name = 'orders'
    login_url = reverse_lazy('login-page')
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    

class DeleteOrderView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'delete_order.html'
    success_url = reverse_lazy('view_order')
    login_url = reverse_lazy('login-page')
    