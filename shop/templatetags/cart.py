from django import template
register = template.Library()



@register.filter(name='in_cart')

def in_cart(product, cart):
  keys = cart.keys()
  
  for id in keys :
    if int(id) == product.id:
      return True

  
@register.filter(name='quantity')

def quantity(product, cart):
  keys = cart.keys()
  
  for id in keys :
    if int(id) == product.id:
      return cart.get(id)
      
  
  
@register.filter(name='total')

def total(product, cart):
    return product.price * quantity(product,cart)
  


  
@register.filter(name='total_cart')

def total_cart(product, cart):
  sum = 0
  for product in product :
    sum += total(product, cart)
  return sum
  