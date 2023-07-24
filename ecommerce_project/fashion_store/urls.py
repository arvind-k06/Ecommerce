
from django.urls import path
from .views import *

app_name = 'fashion_store'

urlpatterns = [
    path('categories/', category_list_create_view, name='category-list-create'),
    path('categories/<int:pk>/', category_retrieve_update_delete_view, name='category-retrieve-update-delete'),
    path('products/', product_list_create_view, name='product-list-create'),
    path('products/<int:pk>/', product_retrieve_update_delete_view, name='product-retrieve-update-delete'),
    path('orders/', order_list_create_view, name='order-list-create'),
    path('orders/<int:pk>/', order_retrieve_update_delete_view, name='order-retrieve-update-delete'),
]

"""

---------------------------------   Class Based view URLs -----------------------------------


# fashion_store/urls.py
from django.urls import path
from .views import CategoryListCreateView, ProductListCreateView, OrderListCreateView, CategoryRetrieveUpdateDeleteView

app_name = 'fashion_store'

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name='category-retrieve-update-delete'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]




"""
