from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Category, Customer, Product, Order, OrderItem
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm, ProductForm, OrderForm, OrderItemForm, CustomerForm
# Create your views here.

###########################
#       Category          #
###########################
class CategoryListView(ListView):
    model = Category
    template_name = 'app/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'app/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

###########################
#       Product           #
###########################
class ProductListView(ListView):
    model = Product
    template_name = 'app/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Optimize the query to include related customer data
        return Product.objects.select_related('category')
    
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'app/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'app/Product_form.html'
    success_url = reverse_lazy('Product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'app/Product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

###########################
#       Order             #
###########################
    
class OrderListView(ListView):
    model = Order
    template_name = 'app/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        # Optimize the query to include related customer data
        return Order.objects.select_related('customer')

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'app/order_form.html'
    success_url = reverse_lazy('order_list')
    
class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'app/order_form.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'app/Order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

###########################
#       Order Items       #
###########################
class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'app/order_item_list.html'
    context_object_name = 'orders_item'

class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'app/order_item_form.html'
    success_url = reverse_lazy('order_item_list')

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'app/order_form.html'
    success_url = reverse_lazy('order_item_list')

class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = 'app/Order_Item_confirm_delete.html'
    success_url = reverse_lazy('order_item_list')

###########################
#       Customer          #
###########################
class CustomerListView(ListView):
    model = Customer
    template_name = 'app/customer_list.html'
    context_object_name = 'customers'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'app/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'app/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'app/customer_confirm_delete.html'
    success_url = reverse_lazy('order_item_list')
