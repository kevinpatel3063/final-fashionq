from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("registration", views.registration_Details, name="registration"),
    path("handlelogin", views.handlelogin, name="handlelogin"),
    path("logout", views.handlelogout, name = "logout"),
    path("index", views.index, name="index"),
    
    path("Cart/checkout", views.checkout, name="checkout"),
    # path("cart.html", views.cart, name="cart.html"),
    path("contact", views.contact, name="contact"),
    path("privacy", views.privacy, name="privacy"),
    path("salesreturn", views.salesreturn, name="salesreturn"),
    path("shopdetail", views.shopdetail, name="shopdetail"),
    path("shop/", views.shop, name="shop"),
    path("shop", views.shop, name="shop"),
    path("terms", views.terms, name="terms"),
    path("layout_footer", views.layout_footer, name="layout_footer"),
    path("block_hf", views.block_hf, name="block_hf"),
    path("error", views.error, name="error"),
    path("hello", views.hello, name="hello"),
    path("singleproduct", views.single, name="singleproduct"),
    path("sea", views.sea, name = "sea"),
    path("shop<str:id>", views.singleproduct, name = "singleproduct"),
    path("userdetails", views.userdetails, name = "userdetails"),
    path("yourorder", views.yourorder, name = "yourorder"),
    
    
    #CART...
    
    # path("cart", views.cart, name="cart"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('Cart/cart_details',views.cart_details,name='Cart/cart_details'),
    path('Cart/checkout/placeorder', views.PLACE_ORDER, name='place_order'),
    path('success', views.success,name = 'success'),
    
   
    ]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)