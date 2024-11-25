#defined menu to be printed once code starts running along with the welcome text, defined quer to be brought up to look for specific codes in the list
def menu():
    print("""
          1.Snacks\n
          2.Drinks\n
          3.Candy
          """)
          
def quer():
    return input("Please type code to continue: ").strip().lower()

#a list to put all information of names of food,pricing, and specific code
uscode =[
{
     'name' : "Boritos",
     'code' : "b4",
     'price' : 4.00,
     },
    
{
     'name' : "Geetos",
     'code' : "b7",
     'price' : 3.50,
     },
    
{
     'name' : "Ajman Chips",
     'code' : "b3",
     'price' : 3.00,
     },
    
{
     'name' : "Cringles",
     'code' : "b1",
     'price' : 4.50,
     },
    
{
     'name' : "Poca Cola",
     'code' : "c4",
     'price' : 2.50,
     },
    
{
     'name' : "Epesi",
     'code' : "c5",
     'price' : 3.50,
     },
    
{
     'name' : "Mr Peppr ",
     'code' : "c2",
     'price' : 2.50,
     },
    
{
     'name' : "Canyon Dew",
     'code' : "c1",
     'price' : 3.00,
     },
{
     'name' : "NOTella Bar",
     'code' : "d5",
     'price' : 3.00,
     },
    
{
     'name' : "Sour Patch Guys",
     'code' : "d8",
     'price' : 2.50,
     },
    
{
     'name' : "Somber Joy",
     'code' : "d2",
     'price' : 2.50,
     },
    
{
     'name' : "Thrix",
     'code' : "d9",
     'price' : 3.50,
     },
    ]

print("\n================WELCOME USER================== \nPlease select from the following...")
menu()

#Made an if loop so if user selects # between 1-3 it would display the respective options

c=(int(input("Please select number: ")))
if c==1:
        print("""
              [b4]Boritos   4.00 AED\n
              [b7]Geetos   3.50 AED\n
              [b3]Ajman Chips   3.00 AED\n
              [b1]Cringles   4.50 AED\n
              """)
elif c==2:
        print("""
              [c4]Poca Cola   2.50 AED\n
              [c5]Epesi   3.50 AED\n
              [c2]Mr Peppr   2.50 AED\n
              [c1]Canyon Dew   3.00 AED\n
              """)
elif c==3:
        print("""
              [d5]NOTella Bar   3.00 AED\n
              [d8]Sour Patch Guys   2.50 AED\n
              [d2]Somber Joy   2.50 AED\n
              [d9]Thrix   3.50 AED\n
              """)
else:
        print("invalid #, Please try again.")
        ch=int(input("Press 1 to go back: "))
        if ch==1:
            menu()

#specifically looks for the code from the 'uscode' list
item = None
selcode = quer()


for i in uscode:
    if selcode == i['code'].lower():
            item = i
            
if item is None:    
    print("Invalid Code.")
    ch=int(input("Press 1 to go back: "))
    quer()
    
#price area, where it also calculates your change if you put more than what the price asks
price = item['price']
print(f"\nthe item you selected, {item['name']}, will cost you {price:.2f} AED.")


while True:
    paid = float(input("\nPlease enter the amount of AED paying for: "))
    if paid < price:
       print(f"\nNot enough amount. You need {price - paid:.2f} AED more.")
    else:
     change = paid - price 
     if change > 0:
       print(f"\nThank you for your purchase at Yvizz Vending Machines. Your change is {change:.2f} AED.")
     else:
       print(f"\nThank you for your purchase at Yvizz Vending Machines.Enjoy your {item['name']}")
    break

