from utils import print_message, get_size, order_latte

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = "y"

  drinks = []

  while order_drink == "y":
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)
    
    name = input('Can I get your name please? \n> ')
    print('Thanks, {}! Your order will be ready shortly.'.format(name))

    while True:
      order_drink = input("Would you like to order another drink? (y/n) ")
      if order_drink == "y" or order_drink == "n":
        break
  
  print("OKay, so I have: ")
  for order in drinks:
    print("- ", order)

  print("Your order will be right up! Have a good day :) ")
  


def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
# Define new functions here!
def order_mocha():
  while True:
    res = input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n>")
    if res == 'a':
      return 'peppermint moch'
    elif res == 'b':
      return 'mocha'
    else:
      print_message()

coffee_bot()
