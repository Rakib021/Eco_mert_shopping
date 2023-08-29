from django.shortcuts import render,redirect
from store.models import ProductModel
from .models import CartModel,CartItemModel

# Create your views here.

def cart(request):
    session_id = request.session.session_key
    cartid = CartModel.objects.get(cart_id=session_id)
    cart_id = CartModel.objects.filter(cart_id=session_id).exists()
    if cart_id:
        cart_items =CartItemModel.objects.filter(cart=cartid)
    return render(request,'cart/cart.html',{'cart_items':cart_items})


def add_to_cart(request,product_id):
    product =ProductModel.objects.get(id =product_id)
    session_id = request.session.session_key
    cart_id = CartModel.objects.get(cart_id=session_id)
    
    
    
    
    
    if cart_id:
            cart_item = CartItemModel.objects.filter(product=product)
            if cart_item:
                item = CartItemModel.objects.get(product=product)
                item.quantity+=1
                item.save()
            else:
                item = CartItemModel.objects.create(
                    cart= cart_id,
                    product=product,
                    quantity=1
                )
                item.save()
    else:
        cart = CartModel.objects.create(
            cart_id=session_id
        )
        cart.save()

    
    
    # cart = CartModel.objects.create(cart_id=session_id)
    # cart.save()
 
    return redirect('cart')