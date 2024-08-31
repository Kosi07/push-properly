# We are practicing python ... IT'S AWESOME

print("Hello and Welcome to our Coffee Shop!!!!!!")
idiot = input("Nigga what tf is your name?!!\n")

#Stopping any "Ben" or "Patricia" from entering
#if they have not done enough good deeds
if idiot == "Ben" or idiot == "Patricia":
  evil_status = input("Are you evil, yes or no?\n")
  if evil_status == "yes":
    good_deeds = input("How many good deeds have you done today?\n")
    if int(good_deeds) < 4:
     print("Get TF out Evil " + idiot + "!!")
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
     
#Stopping Loki from entering our coffee shop
elif idiot == "Loki":
   print("LEAVE NOW LOKI!!!!")

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
   

   