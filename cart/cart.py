from ecom_admin.models import Product
class Cart():
    def __init__(self,request):
        self.session =request.session
        cart= self.session.get('cart')

        if 'cart' not in request.session:
            cart= self.session['cart'] = {}

        self.cart=cart
    def add(self, product,qty):
        product_id = str(product.id)
        product_qty = str(qty)

        if product_id in self.cart:
            pass
        else:
   
            self.cart[product_id]= int(product_qty)
            self.session.modified= True
    def __len__(self):
        return len(self.cart)
    
    def get_products(self):

        products_id = self.cart.keys()

        products= Product.objects.filter(id__in =products_id)
        return products
    def item_qty(self):
        qty=self.cart
        return qty
    def cart_total(self):
        qty = self.cart  
        product_ids = self.cart.keys()  
     
        products = Product.objects.filter(id__in=product_ids)  
        cartTotal = 0
       

        for product_id, quantity in qty.items():
            product_id = int(product_id) 
            quantity = int(quantity)  
            # print(f"Product ID: {product_id}, Quantity: {quantity}")

           
            product = next((p for p in products if p.id == product_id), None)
            if product:
                if product.on_sale:
                    item_price = product.sale_price
                else:
                    item_price = product.regular_price

                # Calculate totals
                cartTotal += item_price * quantity
             
                
        return cartTotal
    
    def delete(self,product):
        product_id=str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified= True