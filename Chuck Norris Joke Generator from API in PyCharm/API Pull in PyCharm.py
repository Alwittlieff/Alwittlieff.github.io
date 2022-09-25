# DSC 510
# Week 11
# Programming Assignment Week 11
# Author Alexa Wittlieff
# 11/14/2021

# Assignment Requirements
#Must have a header and welcome message for the user.
#Must have one class called CashRegister.
#Your program will have an instance method called addItem which takes one parameter for price.
#The method should also keep track of the number of items in your cart.
#Your program should have two getter methods.
#getTotal – returns totalPrice
#getCount – returns the itemCount of the cart
#Must create an instance of the CashRegister class.
#Your program should have a loop which allows the user to continue to add items to the cart until they request to quit.
#Your program should print the total number of items in the cart.
#Your program should print the total $ amount of the cart.
#The output should be formatted as currency.
#Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.

import locale
locale.setlocale(locale.LC_ALL, '')

class CashRegister:

    def __init__ (self):
        self.itemCount = 0
        self.totalPrice = 0.0

    def addItem (self, itemCount, totalPrice):
        self.itemCount = itemCount + 1
        self.totalPrice = totalPrice #+itemPrice

    def getTotal(self):
        return self.totalPrice

    def getTotal(self):
        return locale.currency(self.totalPrice, grouping=True)

    def clearCart(self):
        self.itemCount = 0
        self.totalPrice = 0.0

def main():
    print("Welcome to the Cash Register Calculator!")
    itemPrice = int(input("\nPlease enter the item's price or type x to complete your purchase. "))
    register = CashRegister()
    register.addItem(itemPrice, totalPrice)
    #Increment the number of items in the cart and add that amount to the total
    #Create Loop to Add Items
    while itemPrice != 'x':
        try:
            item_price = float(itemPrice)
            register.addItem(itemPrice)
            itemPrice = input("\nPlease enter the item's price or type x to complete your purchase. ")
            itemPrice.lower()
        except:
            itemPrice = int(input("\nPlease enter the item's price or type x to complete your purchase. "))
            itemPrice = itemPrice.lower()

    #At the end get the totals and print the total number of items and total price
    register.getTotal()
    register.getCount()
    print("Purchase entries complete!")
    print(CashRegister.getCount())
    print(CashRegister.getTotal())

if __name__ == "__main__":
    main()
