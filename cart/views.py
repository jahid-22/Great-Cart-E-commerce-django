from django.shortcuts import render, get_object_or_404
from store.models import Product
from cart.models import Catagory
# Create your views here.

# Home view
def home(request):
    product = Product.objects.all().filter(is_available=True) # To bring just availabe product
    context = {
        'prducts':product
    }
    return render(request, 'cart/index.html',context)

# cart view
def cart(request):
    return render(request, 'cart/cart.html')

# dashboard view
def dashboard(request):
    return render(request, 'cart/dashboard.html')

# placeorder
def placeorder(request):
    return render(request, 'cart/place-order.html')

# product detail
def product_detail(request,catagory_slug, product_slug):
    try:
        single_product = Product.objects.get(catagory__slug = catagory_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product':single_product,
    }
    return render(request, 'cart/product-detail.html', context)

# register view
def register(request):
    return render(request, 'cart/register.html')

# search result
def seartch_result(request):
    return render(request, 'cart/search-result.html')

# sign in 
def sign_in(request):
    return render(request, 'cart/signin.html')

# store
def store(request, catagory_slug = None):
    catagories = None
    products   = None
    
    if catagory_slug != None:
        catagories = get_object_or_404(Catagory, slug = catagory_slug)
        products = Product.objects.filter(catagory=catagories, is_available=True)
        product_count = products.count()
    
    else:  
        products = Product.objects.all().filter(is_available=True) # To bring just availabe product
        product_count = products.count()
        
    context = {
            'prducts':products,
            'product_count':product_count,
    }
    
    return render(request, 'cart/store.html',context)