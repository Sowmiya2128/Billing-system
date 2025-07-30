from django.urls import path
from .import views
urlpatterns =[
    path('',views.Home_page,name='Home-page'),
    path('add-product/', views.add_product, name='add-product'),
    path('add-customer/', views.add_customer, name='add-customer'),
    path('add-sale/', views.add_sale, name='add-sale'),
    path('product-list',views.product_list,name ='product-list'),
    path('customer-list',views.customer_list,name ='customer-list'),
    path('sale-list',views.sale_list,name ='sale-list'),
    path('products/add/',views.add_product,name='add-product'),
    path('products',views.product_list,name ='product-list'),
    path('customers/add/',views.add_customer,name='add-customer'),
    path('customers/',views.customer_list,name ='customer-list'),
    path('sales/add/',views.add_sale,name='add-sale'),
    path('sales/',views.sale_list,name ='sale-list'),
]

