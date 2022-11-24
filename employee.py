#Name: Leo Torres
   
import datetime

## define global variables ##
# define tax rate and prices
FEDERAL_TAX_RATE = .12
STATE_TAX_RATE = .03
SOCIAL_TAX_RATE = .062
MEDICARE_TAX_RATE = .0145
CASHIER = 16.50
STOCKER = 15.75
JANITOR = 15.75
MAINTENANCE = 19.50

# define global variables
gross_pay = 0
deduction_rate1 = 0
deduction_rate2 = 0
deduction_rate3 = 0
deduction_rate4 = 0
total_deductions = 0
net_pay = 0
job_category = 0
num_hours = 0

## define program functions ##
def main():
    another_pay_stub = True
    while another_pay_stub:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("Would you like to see another employee rate? (Y/N)")
        if yesno.upper() == "N": 
            another_pay_stub = False 
            print("Thank for checking F.F.M. weekly pay")
            return()

def get_user_data():
    global job_category, num_hours
    print("Job Categories:")
    print("\t C for Cashier")
    print("\t S for Stocker")
    print("\t J for Janitor")
    print("\t M for Maintenance")

    job_category = input("\nJob: ")
    num_hours = int(input("Number of hours worked: "))

def perform_calculations():
    global gross_pay, deduction_rate1, deduction_rate2, deduction_rate3, deduction_rate4, total_deductions, net_pay, num_hours
    if job_category.upper() == "C":
        gross_pay = num_hours * CASHIER
    if job_category.upper() == "S":
        gross_pay = num_hours * STOCKER
    if job_category.upper() == "J":
        gross_pay = num_hours * JANITOR
    if job_category.upper() == "M":
        gross_pay = num_hours * MAINTENANCE        
    deduction_rate1 = gross_pay * FEDERAL_TAX_RATE
    deduction_rate2 = gross_pay * STATE_TAX_RATE
    deduction_rate3 = gross_pay * SOCIAL_TAX_RATE
    deduction_rate4 = gross_pay * MEDICARE_TAX_RATE
    total_deductions = deduction_rate1 + deduction_rate2 + deduction_rate3 + deduction_rate4
    net_pay = gross_pay - total_deductions
    
def display_results():
    print('----------------------------------------')
    print('******** Fresh Food Marketplace ********')
    print('************** Weekly Pay **************')
    print('----------------------------------------')
    print('Number of Hours Worked:         '+format (num_hours,'8,d'))    
    print('Federal Income:                $'+format (deduction_rate1,'8,.2f'))
    print('State Income:                  $'+format (deduction_rate2,'8,.2f'))
    print('Social Security:               $'+format (deduction_rate3,'8,.2f'))
    print('Medicare:                      $'+format (deduction_rate4,'8,.2f'))
    print('Total Deduction:               $'+format (total_deductions,'8,.2f'))
    print('Gross Pay:                     $'+format (gross_pay,'8,.2f'))
    print('Net Pay:                       $'+format (net_pay,'8,.2f'))
    print('----------------------------------------')
    print(str(datetime.datetime.now()))

## call on main program to execute ##
main() 