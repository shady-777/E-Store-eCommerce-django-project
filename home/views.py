from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *


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


def contact(request):
    views = {}
    views['information'] = Information.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Users.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        data.save()
        return render(request, 'contact.html', views)
    return render(request, 'contact.html', views)

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
