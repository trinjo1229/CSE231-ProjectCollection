##############################################################################
#   Computer Project #2
#   
#   Alogorithm
#       Ask user if they'd like to continue the trasaction 
#       While they say yes 
#           ask for the correct customer code, the start of their odometer, \
#           and the end of their odomoeter 
#           use information to calculate how many miles they drove and, how \
#           much money they owe the company
#       display the information the customer put in, how many miles they \
#       drove, and how many dollars they owe the company 
#       ask if they'd like to continue, if not then thank them
##############################################################################

import math
BASE_B = 40 # base charge for budget package 
BASE_D = 60 # base charge for daily package 
BASE_W = 190 # base charge for weekly package 
MI_CHARGE = .25 # charge per extra mile you drive after given limit
money_due = 0
mi_difference = 0
mi_total = 0
NUM_DAYS_IN_WEEK = 7 # number of days in a week 
weeks = 0
MI_LI_PER_DAY_D = 100 # the limit of miles you can drive per day in package D without extra charge
MI_LI_PER_WEEK_W = 1500 # the limit of miles you can drive per week in package W without extra charge
WHEN_ODOMETER_RESETS = 1000000 # when the odometer resets to zero
ADD_CHARGE_AF_LI_W = 200 # added charge per week after 1500 miles/week limit is reached for package W
MAX_NO_EXTRA_CHARGE_W = 900 # the maximum miles you can drive with no extra charge
CHARGE_PER_WEEK_MORE_MIN = 100 # charge per week when you drive more than 900 but less than 1500 miles
 
print("\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)")
print()
answer = input("Would you like to continue (Y/N)? ") 
print()

while answer == str("Y"):
    code = input("Customer code (BDW): ")
    if code =='B' or code == 'D' or code == 'W':
        print()
        num_days_str = input("Number of days: ")
        num_days_flt = float(num_days_str)
        s_odometer_str = input("Odometer reading at the start: ")
        s_odometer_flt = float(s_odometer_str)
        e_odometer_str = input("Odometer reading at the end: ")
        e_odometer_flt = float(e_odometer_str)
    else:
        print("\n\t*** Invalid customer code. Try again. ***")
        continue
     
    if e_odometer_flt > s_odometer_flt: 
        mi_total = (e_odometer_flt - s_odometer_flt) * 1.0e-1 # use scientific notation to account for the tenth of a mile
        weeks = math.ceil(num_days_flt / NUM_DAYS_IN_WEEK)
        
    else: 
        until_reset = WHEN_ODOMETER_RESETS - s_odometer_flt 
        mi_total = (until_reset + e_odometer_flt) * 1.0e-1 # use scientific notation to account for the tenth of a mile
        weeks = math.ceil(num_days_flt / NUM_DAYS_IN_WEEK)
    
    if code == 'B':
        money_due = (BASE_B * num_days_flt) + (MI_CHARGE * mi_total)
        
    elif code == 'D' and mi_total > MI_LI_PER_DAY_D: 
        mi_difference = mi_total - (MI_LI_PER_DAY_D * num_days_flt)
        money_due = (BASE_D * num_days_flt) + (mi_difference * MI_CHARGE)
        
    elif code == 'D' and mi_total <= MI_LI_PER_DAY_D:
        money_due = (BASE_D * num_days_flt)
        
    elif code == 'W' and (mi_total / weeks) > MI_LI_PER_WEEK_W: 
        money_due = ((mi_total - (MI_LI_PER_WEEK_W * weeks)) * MI_CHARGE) \
            + (ADD_CHARGE_AF_LI_W * weeks) + (BASE_W * weeks) 
        
    elif code == 'W' and MAX_NO_EXTRA_CHARGE_W < (mi_total / weeks) <= MI_LI_PER_WEEK_W:
        money_due = (BASE_W * weeks) + (CHARGE_PER_WEEK_MORE_MIN * weeks)
        
    elif code == 'W' and (mi_total / weeks) <= MAX_NO_EXTRA_CHARGE_W:
        money_due = (BASE_W * weeks)
                    
    print("\nCustomer summary:",
          "\n\tclassification code:",(code),
          "\n\trental period (days):",int((num_days_flt)),
          "\n\todometer reading at start:",int(s_odometer_str),
          "\n\todometer reading at end:  ",int(e_odometer_str),
          "\n\tnumber of miles driven: ",round((mi_total),1),
          "\n\tamount due: $",(float(money_due)))
    print()
    answer = input("Would you like to continue (Y/N)? ")
    print()
else: 
    print("Thank you for your loyalty.")
