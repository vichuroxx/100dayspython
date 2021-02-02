from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

userin=Menu()
#menulist=MenuItem()
coffeemachine=CoffeeMaker()
moneyhandle=MoneyMachine()

machine_status="On"

while machine_status=="On":
  user=input("What Do you like to have ? :- "+userin.get_items()+" :-")
  if user=="Off":
    machine_status="Off"
  elif userin.find_drink(user)!=None:
    print(coffeemachine.report())
    object=userin.find_drink(user)
    if coffeemachine.is_resource_sufficient(object)==True:
      print("sufficient resouce")
      if moneyhandle.make_payment(object.cost)==True:
        coffeemachine.make_coffee(object)
    else:
      print("Not enought resources")
