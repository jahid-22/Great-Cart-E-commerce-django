from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('placeorder/', views.placeorder, name="placeorder"),
    path('product_detail/<slug:catagory_slug>/<slug:product_slug>/', views.product_detail, name="product_detail"),
    path('register/', views.register, name="register"),
    path('seartch_result/', views.seartch_result, name="seartch_result"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('store/<slug:catagory_slug>/', views.store, name="products_by_cata"),
    path('store/', views.store, name="store"),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
