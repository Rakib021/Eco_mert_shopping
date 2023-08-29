from django.shortcuts import render,get_object_or_404
from .models import ProductModel
from category.models import CategoryModel
from django.core.paginator import Paginator

# Create your views here

def store(request,category_slug = None):
    category = None
    
    if category_slug:
        category =get_object_or_404(CategoryModel,slug = category_slug)
        products = ProductModel.objects.filter(is_available = True,category = category)
        page =request.GET.get('page')
        paginator = Paginator(products,1)
        page_product = paginator.get_page(page)
        
    else:
         products = ProductModel.objects.filter(is_available = True)
         paginator = Paginator(products,3)
         page =request.GET.get('page')
         page_product = paginator.get_page(page)

          
    categories = CategoryModel.objects.all()
    context ={'products':page_product,'categories':categories}
    
    print(category)
    
    return render(request,'store/store.html',context)

#product detail show
def product_detail(request,category_slug,product_slug):
    single_product = ProductModel.objects.get(category__slug=category_slug,slug=product_slug)

    return render(request,'store/product-detail.html',{'product':single_product})
    
