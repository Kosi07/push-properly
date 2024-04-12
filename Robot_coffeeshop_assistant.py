# We are practicing python ... IT'S AWESOME
#print("Hello World. \n" + "I am Iron Man. \n" + "No, I am Tony Stark.")
#print("Poppy\n" * 10)
print("Hello and Welcome to our Coffee Shop!!!!!!")
idiot = input("Nigga what tf is your name?!!\n")

#Stopping Ben from entering
if idiot == "Ben":
  evil_status = input("Are you evil, yes or no?\n")
  if evil_status == "yes":
    print("Get TF out Evil Ben!")
  else:
   print("What would you like to order?")
   menu = input("Black Coffee, Tea, Latte or Expresso?\n")

   
   print("Hello " + idiot + ". Thanks for coming :)\n")

   price = 0
   if menu == "Black Coffee":
      price = 3
      quantity = input("How many cups would you like?\n")
      print("Your " + menu + " will be ready in 5 minutes ;)")
      total = price * int(quantity)
      print("Your total comes down to " + "$" + str(total))


   elif menu == "Tea":
      price = 5
      quantity = input("How many cups would you like?\n")
      print("Your " + menu + " will be ready in 5 minutes ;)")
      total = price * int(quantity)
      print("Your total comes down to " + "$" + str(total))

   elif menu == "Latte":
      price = 5
      quantity = input("How many cups would you like?\n")
      print("Your " + menu + " will be ready in 5 minutes ;)")
      total = price * int(quantity)
      print("Your total comes down to " + "$" + str(total))

   elif menu == "Expresso":
      price = 13 
      quantity = input("How many cups would you like?\n")
      print("Your " + menu + " will be ready in 5 minutes ;)")
      total = price * int(quantity)
      print("Your total comes down to " + "$" + str(total))

   else:
     print("Sorry, we don't have that here :(")
else:
  #Asking for customer's orders
   print("What would you like to order?")
   menu = input("Black Coffee, Tea, Latte or Expresso?\n")

   
   print("Hello " + idiot + ". Thanks for coming :)\n")

   price = 0
   if menu == "Black Coffee":
      price = 3
      quantity = input("How many cups would you like?\n")
      print("Your " + menu + " will be ready in 5 minutes ;)")
      total = price * int(quantity)
      print("Your total comes down to " + "$" + str(total))


   elif menu == "Tea":
      price = 5
      quantity = input("How many cups would you like?\n")
      print("Your " + menu + " will be ready in 5 minutes ;)")
      total = price * int(quantity)
      print("Your total comes down to " + "$" + str(total))

   elif menu == "Latte":
      price = 5
      quantity = input("How many cups would you like?\n")
      print("Your " + menu + " will be ready in 5 minutes ;)")
      total = price * int(quantity)
      print("Your total comes down to " + "$" + str(total))

   elif menu == "Expresso":
      price = 13 
      quantity = input("How many cups would you like?\n")
      print("Your " + menu + " will be ready in 5 minutes ;)")
      total = price * int(quantity)
      print("Your total comes down to " + "$" + str(total))

   else:
     print("Sorry, we don't have that here :(")
   

   