from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.DishView.as_view(), name='dish_list'),
    path('dish/<int:pk>/', views.DishDetailView.as_view()),
    path('cart', views.ShopcartView.as_view(), name='shopcart')
]