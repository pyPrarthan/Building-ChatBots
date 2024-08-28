# Define your functions
from outcome import Value


def coffee_bot():
  print("Welcome to the Cafe!")

  size = get_size()  
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {}!'.format(size, drink_type))

  name = input("Can I get your name please? ")
  print("Thanks, " + name + "! Your drink will be ready shortly.")
 
  

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  res = input("What kind of drink would you like ? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>")
  if res == 'a':
    return "brewed coffee"
  elif res == 'b':
    return "mocha"
  elif res == 'c':
    return order_lattee()
  else:
    print_message()
    return get_drink_type()

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return "small"
  elif res == 'b':
    return "medium"
  elif res == 'c':
    return "large"
  else:
    print_message()
    return get_size()

def order_lattee():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>")
  if res == 'a':
    #print("Your coffee with 2% milk coming right up!!!")
    return "2% milk"
  elif res == 'b':
    return "non-fat milk"
  elif res == 'c':
    return "soy milk"
  else:
    print_message()
    return order_lattee()
  

# Call coffee_bot()!
coffee_bot()
