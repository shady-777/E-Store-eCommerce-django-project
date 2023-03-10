from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['brands'] = Brand.objects.all()
    views['sale_products'] = Product.objects.filter(label='sale', stock='In stock')


class HomeView(BaseView):

    def get(self, request):
        self.views
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['new_products'] = Product.objects.filter(label='new', stock='In stock')
        self.views['hot_products'] = Product.objects.filter(label='hot', stock='In stock')
        self.views['feedbacks'] = Feedback.objects.all()
        self.views['calls'] = Callus.objects.all()
        return render(request, 'index.html', self.views)


class CategoryView(BaseView):

    def get(self, request, slug):
        ids = Category.objects.get(slug=slug).id
        self.views['cat_product'] = Product.objects.filter(category_id=ids)
        return render(request, 'category.html', self.views)


class BrandView(BaseView):

    def get(self, request, slug):
        ids = Brand.objects.get(slug=slug).id
        self.views['brand_product'] = Product.objects.filter(brand_id=ids)
        return render(request, 'brand.html', self.views)


class SearchView(BaseView):

    def get(self, request):
        query = request.GET.get('query')
        if query != '':
            self.views['search_product'] = Product.objects.filter(name__icontains=query)
        else:
            return redirect('/')
        return render(request, 'search.html', self.views)


class ProductDetailView(BaseView):

    def get(self, request, slug):
        self.views['product_detail'] = Product.objects.filter(slug=slug)
        subcat_id = Product.objects.get(slug=slug).subcategory_id
        product_id = Product.objects.get(slug=slug).id
        self.views['product_image'] = ProductImage.objects.filter(product_id=product_id)
        self.views['subcat_product'] = Product.objects.filter(subcategory_id=subcat_id)
        return render(request, 'product-detail.html', self.views)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken!')
                return redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'The email is already taken!')
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password

                )
                data.save()
                return render(request, '/accounts/login')
        else:
            messages.error(request, 'Password does not match !')
            return redirect('/signup')

    return render(request, 'signup.html')


class ProductListView(BaseView):

    def get(self, request):
        return render(request, 'product-list.html', self.views)


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
def contact(request):
    return render(request, 'contact.html')
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
