from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
                     ProductListView,ProductCreateView,ProductUpdateView, ProductDeleteView,
                     OrderListView,OrderCreateView, OrderUpdateView, OrderDeleteView,
                     OrderItemListView, OrderItemCreateView, OrderItemUpdateView, OrderItemDeleteView,
                     CustomerListView,CustomerCreateView,CustomerUpdateView,CustomerDeleteView)

# URL patterns
urlpatterns = [   
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/add', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('order/add', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/edit', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete', OrderDeleteView.as_view(), name='order_delete'),
    path('orderitems/', OrderItemListView.as_view(), name='order_item_list'),
    path('orderitem/add', OrderItemCreateView.as_view(), name='order_item_create'),
    path('orderitem/<int:pk>/edit', OrderItemUpdateView.as_view(), name='order_item_update'),
    path('orderitem/<int:pk>/delete', OrderItemDeleteView.as_view(), name='order_item_delete'),
    path('customers/',CustomerListView.as_view(),name='customer_list'),
    path('customer/add', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>/edit', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete', CustomerDeleteView.as_view(), name='customer_delete'),
]

