from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.DishView.as_view(), name='main_page'),
    path('dish/<int:pk>/', views.DishDetailView.as_view(), name='dish_detail'),
    path('shopcart', views.ShopcartView.as_view(), name='shopcart'),
    path('shopcart-create/', views.ShopcartCreateView.as_view(), name='shopcart-create'),
    path("shopcart-update/<int:pk>/", views.ShopcartUpdateView.as_view(), name="shopcart-update"),
    path("shopcart-delete/<int:pk>/", views.ShopcartDeleteView.as_view(), name="shopcart-delete"),
    path('tom', views.PayView.as_view(), name='tom')
]