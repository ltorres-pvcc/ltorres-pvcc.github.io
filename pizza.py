#Name: Leo Torres
#Program Purpose: This program finds the cost of a pizza order
#   Price for a small pizza: 9.99
#   Price for a medium pizza: 12.99
#   Price for a large pizza: 14.99
#   Price for a extra large pizza: 17.99
#   Sales tax rate: 5.5%
   
import datetime

## define global variables ##
# define tax rate and prices
SALES_TAX_RATE = .055
S_PIZZA = 9.99
M_PIZZA = 12.99
L_PIZZA = 14.99
X_PIZZA = 17.99

# define global variables
num_pizza = 0
pizza_size = 0
subtotal = 0
sales_tax = 0
total = 0

## define program functions ##
def main():
    another_order = True
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("Would you like to order again? (Y/N)")
        if yesno.upper() == "N": 
            another_order = False 
            print("Thank for ordering at Palermo Pizza")
            return()

def get_user_data():
    global pizza_size, num_pizza
    print("Palermo Pizza Sizes:")
    print("\t S for Small")
    print("\t M for Medium")
    print("\t L for Large")
    print("\t X for Extra Large")

    pizza_size = input("\nPizza size: ")
    num_pizza = int(input("Number of pizzas: "))

def perform_calculations():
    global subtotal, sales_tax, total, pizza_size, num_pizza
    if pizza_size.upper() == "S":
        subtotal = num_pizza * S_PIZZA
    if pizza_size.upper() == "M":
        subtotal = num_pizza * M_PIZZA
    if pizza_size.upper() == "L":
        subtotal = num_pizza * L_PIZZA
    if pizza_size.upper() == "X":
        subtotal = num_pizza * X_PIZZA        
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    
def display_results():
    print('--------------------------------')
    print('******** PALERMO PIZZAS ********')
    print('Best Homemade Pizzas in the City')
    print('--------------------------------')
    print('Pizza         $'+format (subtotal,'8,.2f'))
    print('Sales Tax     $'+format (sales_tax,'8,.2f'))
    print('Total         $'+format (total,'8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

## call on main program to execute ##
main() 