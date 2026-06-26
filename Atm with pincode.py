atm=5000

w=int(input("Enter the withdraw Amount:-"))

if atm>=w:
    pin=int(input("Enter the pin:-"))
    if pin==6295:
       atm=atm-w
       print("Transaction Successfull")
       print("Your available Balance is:-",atm)
    else:
       print("invalid Pin")
else:
     print("Insufficient Balance")

