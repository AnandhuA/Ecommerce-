from shop.models import products,category
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View

# Create your views here.
    

class Home(View):
   
  
  def get(self,req):
 
    categorys = category.objects.all()
    categoryId = req.GET.get('category')
    cart = req.session.get('cart')
      
    if categoryId :
      product = products.objects.filter(category=categoryId)
 
    else :
      product = products.objects.all()
      
    if not cart:
      req.session['cart'] = {}
    
    return render(req,'home.html',{
      'product':product, 
      'categorys':categorys
    })
    
    
  def post(self,req):
    
    product = req.POST.get('product')
    remove = req.POST.get('remove')
    cart = req.session.get('cart')
    
    if req.user.is_authenticated :
      if product :
        if cart :
          cart[product] = 1
        else :
          cart = {}
          cart[product] = 1
        
      elif remove :
        cart.pop(remove)
        
    else :
      messages.error(req, "please login!!")
      return redirect( 'login')
      
   
    req.session['cart'] = cart
    return redirect ('home') 
      
class Cart(View):
  
  def get(self, req):
    
    if req.user.is_authenticated :
      ids = list(req.session.get('cart').keys())
      product=products.objects.filter(id__in = ids)
    
      return render(req, 'cart.html',{ 'product':product })
    
    else :
      messages.error(req, "please login!!")
      return redirect( 'login')
      
 
  def post(self, req):
    
    remove = req.POST.get('remove')
    cart = req.session.get('cart')
    quantity_plus = req.POST.get('quantity_plus')
    quantity_minus =req.POST.get('quantity_minus')
   

    if remove :
      cart.pop(remove)
      req.session['cart'] = cart
     
    elif quantity_plus :
      quantity = cart.get(quantity_plus)
      cart[quantity_plus] = quantity + 1
      req.session['cart'] = cart

    elif quantity_minus :
      quantity = cart.get(quantity_minus)
      
      if quantity == 1 :
        cart.pop(quantity_minus)
        req.session['cart'] = cart

      else :  
        cart[quantity_minus] = quantity - 1
        req.session['cart'] = cart
      
    return redirect ('cart') 
    
class Single(View):
  
  def get(self, req, product_id):
    
    product_id =products.objects.get(id=product_id)
    
    return render(req, 'single.html', {
      'product':product_id
    })
    
    
  def post(self, req, product_id):
    
    product = req.POST.get('product')
    remove = req.POST.get('remove')
    cart = req.session.get('cart')
    quantity_plus = req.POST.get('quantity_plus')
    quantity_minus =req.POST.get('quantity_minus')
    
    if req.user.is_authenticated :
      if product :
        if cart :
          cart[product] = 1
        else :
          cart = {}
          cart[product] = 1
        
      elif remove :
        cart.pop(remove)
      
    else :
      messages.error(req, "please login!!")
      return redirect( 'login')
   
    req.session['cart'] = cart
    return redirect ('single',product_id) 
