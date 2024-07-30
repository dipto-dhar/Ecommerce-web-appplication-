from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .cart import Cart
from ecom_admin.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    cart = Cart(request)
    cart_items = cart.get_products
    qty = cart.item_qty
    return render(request, 'store/cart.html', {'products': cart_items, 'qty': qty})

def add_to_cart(request):
    if request.method == 'POST':
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        product_qty = int(request.POST.get('item_qty'))
        if product_id in request.session.get('cart', {}):
            messages(request,'This Item is already in your cart')
        else:
            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product, qty=product_qty)
            
            cart_quantity = cart.__len__()
            response = JsonResponse({'qty': cart_quantity})
            return response
    return JsonResponse({'error': 'Invalid request'}, status=400)

def update_cart(request):
    if request.method == 'POST':
        try:
            product_id = str(request.POST.get('product_id'))  # Ensure product_id is a string
            action = request.POST.get('action')
            
            # Retrieve the cart from the session
            cart = request.session.get('cart', {})
            print(f"Cart contents before update: {cart}")
            print(f"Incoming product_id: {product_id}")

            if not isinstance(cart, dict):
                raise TypeError("Cart should be a dictionary")

            # Retrieve the product
            product = get_object_or_404(Product, id=product_id)
            
            # Check if the product_id is in the cart
            if product_id in cart:
                if action == 'increase':
                    cart[product_id] += 1
                elif action == 'decrease' and cart[product_id] > 1:
                    cart[product_id] -= 1
                else:
                    return JsonResponse({'error': 'Invalid action or insufficient quantity'}, status=400)
                
                # Save the updated cart in the session
                request.session['cart'] = cart
                request.session.modified = True

                # Calculate the new total price
                # total_price = sum(
                #     Product.objects.get(id=prod_id).price * qty
                #     for prod_id, qty in cart.items()
                # )

                return JsonResponse({'new_quantity': cart[product_id], })
            else:
                return JsonResponse({'error': 'Product not found in cart'}, status=400)

        except ValueError:
            return JsonResponse({'error': 'Invalid product ID'}, status=400)
        except TypeError as te:
            return JsonResponse({'error': str(te)}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)





def delete_cart(request):
    if request.method == 'POST':
        cart = Cart(request)
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
    return render(request,'store/cart.html')