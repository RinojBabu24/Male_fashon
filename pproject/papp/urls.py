
from . import views
from django.contrib import admin
from django.urls import path

app_name = 'papp'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shopview/<str:slug>/', views.shop, name='shopview'),
    path('productview/<str:cate_slug>/<str:prod_slug>/', views.productview, name="productview"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    

    path('checkout/', views.checkout, name='checkout'),
    path('shoppingcart/', views.shoppingcart, name='shoppingcart'),
    path('addtocart/<str:prod_slug>/', views.addtocart, name='addtocart'),
    path('removefromcart/<int:item_id>/', views.removefromcart, name='removefromcart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('final/', views.final, name='final'),
    path('search/',views.search, name='search'),
    
    
    
]
