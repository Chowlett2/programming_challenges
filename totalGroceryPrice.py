'''Create a function that takes a list of dictionaries (groceries) which 
calculates the total price and returns it as a number. A grocery dictionary has 
a product, a quantity and a price, for example:

{
  "product": "Milk",
  "quantity": 1,
  "price": 1.50
}
'''

def get_total_price(groceries):
    total = 0
    for i in groceries:
        total += i.get('quantity') * i.get('price')
    return round(total, 2)