# We are practicing python ... IT'S AWESOME
#print("Hello World. \n" + "I am Iron Man. \n" + "No, I am Tony Stark.")
#print("Poppy\n" * 10)
print("Hello and Welcome to our Coffee Shop!!!!!!")
idiot = input("Nigga what tf is your name?!!\n")

#Stopping Ben from entering
if idiot == "Ben":
    print("Get TF out Evil Ben!" )
else:
  #Asking for customer's orders
   print("What would you like to order?")
   menu = input("Coffee or Tea?\n")

   quantity = input("How many cups would you like?\n")

   print("Hello " + idiot + ". Thanks for coming :)\n")

   print("Your " + menu + " will be ready in 5 minutes ;)")

   price = 8
   total = price * int(quantity)
   print("Your total comes down to " + "$" + str(total))