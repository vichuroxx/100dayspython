flag=0
dict={}
while flag==0:
    temp={}
    name=input("Enter name of bidder :-")
    amount=input("Enter the bid amount :-")
    temp["name"]=name
    temp["amount"]=amount
    dict["bidder"]=temp
    
    get=input("Do you have more bidders? (y/n) :-")
    if(get=="n"):
        flag=1

for item in dict:
    largest=0
    if(int(item["amount"])>largest):
        largest=item["amount"]
        name=item["name"]
        
print(f"{name} bidded the largest amount of {largest} Rs")
