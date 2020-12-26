from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from shop.models import products
from login.form import custom_user
from login.models import order

# Create your views here.


class Login(View):
  
  def get(self, req):
    
    form = AuthenticationForm()
    return render(req, 'login.html', {'form' : form})
    
  def post(self,req):
    
    form = AuthenticationForm(data = req.POST)
    if form.is_valid() :
      user = form.get_user()
      login(req, user)
      return redirect ('home')
      
    return render(req, 'login.html', {'form' : form})
    

class Logout(View):
  
  def get(self,req):
    
    logout (req)
    return redirect ('home')


class Sign_Up(View):
  
  def get(self, req):
    
    form = custom_user()
    return render(req,'register.html', {'form':form})

  def post(self, req):
    form = custom_user(req.POST)
    if form.is_valid() :
      form.save()
      login(req, user)
      return redirect ('home')
      
    return render(req,'register.html', {'form' : form })


class BuyNow(View):
    
  def post (self, req, product_id):
   
    product_id =products.objects.get(id=product_id)
    email = req.POST.get('email')
    address = req.POST.get('address')
    place = req.POST.get('place')
    city = req.POST.get('city')
    phone = req.POST.get('phone')
    customer = req.user.first_name
    
    data = {
        'email': email,
        'address': address,
        'place': place,
        'city': city,
        'phone': phone,
        'product':product_id
       }
    Order = order(
        customer = customer,
        products = product_id,
        product_name = product_id.name,
        address = address,
        place = place,
        city = city,
        phone = phone,
        price = product_id.price
         )
    Order.save()
    
    return render (req, 'buynow.html', data)
      
class CheckOut(View):
  
  def post (self, req):
    
    ids = list(req.session.get('cart').keys())
    cart = req.session.get('cart')
    product=products.objects.filter(id__in = ids)
    email = req.POST.get('email')
    address = req.POST.get('address')
    place = req.POST.get('place')
    city = req.POST.get('city')
    phone = req.POST.get('phone')
    customer = req.user.first_name
    
    data = {
        'email': email,
        'address': address,
        'place': place,
        'city': city,
        'phone': phone,
        'product':product
       }
    for product in product :
      Order = order(
        customer = customer,
        products = product,
        product_name = product.name,
        address = address,
        place = place,
        city = city,
        phone = phone,
        price = product.price,
        quantity = cart.get(str(product.id))
         )
      Order.save()
    
    req.session['cart'] = {}
    return render (req, 'buynow.html', data)
  


class Account(View):
  
  def get(self, req):
    
    if req.user.is_authenticated :
      return render (req, 'account.html')
      
    else :
      messages.error(req, "please login!!")
      return redirect('login')

      