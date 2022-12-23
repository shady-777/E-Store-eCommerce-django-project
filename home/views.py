from django.shortcuts import render
from django.views.generic import View
from .models import *


# Create your views here.
class BaseView(View):
    views = {}


class HomeView(BaseView):

    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['new_products'] = Product.objects.filter(label='new', stock = 'In stock')
        self.views['hot_products'] = Product.objects.filter(label='hot', stock = 'In stock')
        self.views['sale_products'] = Product.objects.filter(label='sale', stock = 'In stock')
        return render(request, 'index.html', self.views)

# def home(request):
#     return render(request, 'index.html')
#
#
# def cart(request):
#     return render(request, 'cart.html')
#
#
# def checkout(request):
#     return render(request, 'checkout.html')
#
#
# def contact(request):
#     return render(request, 'contact.html')
#
#
# def login(request):
#     return render(request, 'login.html')
#
#
# def my_account(request):
#     return render(request, 'my-account.html')
#
#
# def product_detail(request):
#     return render(request, 'product-detail.html')
#
#
# def product_list(request):
#     return render(request, 'product-list.html')
#
#
# def wishlist(request):
#     return render(request, 'wishlist.html')
