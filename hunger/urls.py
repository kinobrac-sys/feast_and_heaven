from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.DishView.as_view(), name='main_page'),
    path('dish/<int:pk>/', views.DishDetailView.as_view(), name='dish_detail'),
    #path('cart', views.ShopcartView.as_view(), name='shopcart')
]