donext="n"

        
def calcu(op1,op2,operation):
    if(operation=="+"):
        return(op1+op2)
    elif(operation=="*"):
        return(op1*op2)
    elif(operation=="/"):
        return(op1/op2)
    elif(operation=="-"):
        return(op1-op2)

while donext == "n" or donext == "y":
    if(donext == "n"):
        op1 = input("Enter Var 1")
        operator =  input("Enter operator")
        op2 = input("Enter Var 2")
        carryover=calcu(int(op1),int(op2),operator)
        print(carryover)
        donext= input("y - continue \n n - start over")
    elif(donext == "y"):
        op1=carryover
        operator =  input("Enter operator")
        op2 = input("Enter Var 2")
        carryover=calcu(int(op1),int(op2),operator)
        print(carryover)
        donext= input("y - continue \n n - start over")
