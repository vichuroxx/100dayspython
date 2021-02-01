MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def getreport():
    print("Water : " + str(resources["water"]))
    print("Milk : " + str(resources["milk"]))
    print("cofee : " + str(resources["coffee"]))

def resourcesuff(dict):
    for item in dict:
        if item=="water":
            if resources["water"]-dict[item] >-1 :
                print("water sufficient")
            else:
                return "Water"
        elif item == "milk":
            if resources["milk"]-dict[item] >-1 :
                print("Milk sufficient")
            else:
                return "Milk"
        elif item == "coffee":
            if resources["coffee"]-dict[item] >-1 :
                print("Coffee sufficient")
                return True
            else:
                return "Coffee"


def cashcalculator(type):
    quarter=input("How many Quarters ? :- ")
    dimes = input("How many Dimes ? :- ")
    nickles = input("How Many Nickles ? :- ")
    pennies = input("How many Pennies ? :- ")
    total=float(quarter)*0.25+float(dimes)*0.10+float(pennies)*0.01+0.05*float(nickles)
    if total>=MENU[type]["cost"]:
        resources["water"]=resources["water"]-MENU[type]["ingredients"]["water"]
        resources["coffee"]=resources["coffee"] - MENU[type]["ingredients"]["coffee"]
        if type!="espresso":
            resources["milk"]=resources["milk"] - MENU[type]["ingredients"]["milk"]
        change=total-MENU[type]["cost"]
        return True,change
    else:
        print("Refunded ..!! $"+str(round(total,2))+" Not Enough, You Coffee type needs money of $"+str(MENU[type]["cost"]))
        return False,0

caniloop=True
while caniloop==True:
    user = input("What would you like to have (espresso/latte/cappuccino) ? :- ")
    if user == "report":
        print(getreport())
    else:
        sufficient=resourcesuff(MENU[user]["ingredients"])
        if sufficient!=True:
            print("Sorry..!! There is not enough "+str(sufficient))
        else:
            approved,change=cashcalculator(user)
            if approved==True:
                print("Here is Your "+user+" enjoy!!")
                print("change here : $"+str(round(change,2)))

