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
PR_TICKET = 10.99

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

## define program functions ##
def main():
    another_student = True
    while another_student:
        get_user_data()
        perform_calculations()
        display_results()

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets:"))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    
def display_results():
    print('-----------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('-----------------------------')
    print('Tickets       $'+format (subtotal,'8,.2f'))
    print('Sales Tax     $'+format (sales_tax,'8,.2f'))
    print('Total         $'+format (total,'8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

## call on main program to execute ##
main() 