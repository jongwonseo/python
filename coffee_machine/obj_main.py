from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu =Menu()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? ({options}): ")
  
  if choice == 'off':
    is_in = False
  elif choice == 'report':
    coffee_maker.report()
    money_machine.report()
  else:
    # 원하는 커피 menuItem반환
    drink = menu.find_drink() 
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
      coffee_maker.make_coffee(drink)
      

    