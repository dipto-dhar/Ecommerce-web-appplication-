from .cart import Cart

def cart(request):
    return{'cart':Cart(request)}

def cart_summary(request):
    cart = Cart(request)
    cart_items = cart.get_products()
    qty = cart.item_qty()
    total_price=cart.cart_total()
    
    return {'cart_items': cart_items, 'qty': qty,'total_price':total_price}

