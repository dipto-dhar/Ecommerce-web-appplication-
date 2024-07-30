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
            # self.cart[product_id]= {'price':str(product.regular_price)}
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
    
    def delete(self,product):
        product_id=str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified= True