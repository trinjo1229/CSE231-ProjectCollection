###############################################################################
#   Computer Project #5
#
#   Algorithm 
#       The program will ask the user to open up a file. It will then read 
#       through the file limiting its search to lines that focus on the 
#       United States, not including ones focusing on speacific cities. 
#       It will also ignore lines that mention an average.
#       If the line that the program is on meets all of the said requirments 
#       it will print the name of the country, the month that the line refers
#       to, the number of deaths, and a series of D's for the number of people
#       that died, and a series of E's that represent the number of poeple that 
#       were expected to die. Each D or E roughly represents 1,000 people.
###############################################################################


def open_file():
    '''Will open a file, so long as the file exist'''
    answer = "continue"
    file_name = input('Please input a file to use: ') 
    while answer == "continue":
        try:
            file = open(file_name, "r")
            file.readline()
            return file
            answer = "stop" 
    
        except FileNotFoundError: 
            print('Invalid filename, please try again')
            file_name = input('Please input a file to use: ')
            answer = "continue"
        
            
def str_plot(month_int,week_int,n_int,type_str):
    '''will return a sting of the month, the week number, the number of people \
        who've passed on, and a string of D's or E's'''
    month = month_name(month_int)
    n_w_int = convert(n_int)
    if type_str == "deaths":
        num_deaths = "D" * n_w_int
        
    elif type_str == "expected":
        num_deaths = "E" * n_w_int
    return ("{:3s} ({:2d}) {:6,d}: {:s}".format(month, week_int, n_int, num_deaths))
       

def convert(n):
    '''converts a 5 digit number into a float 2 digit number roundedwith one float'''
    n = int(n)
    dec_num = n // 100 / 10 # makes the number into a 3 digit float, one of which being a decimal 
    num_deaths = round(dec_num) # each E or D to be printed is roughly 1,000 people
    return (num_deaths)


def month_name(n):
    '''Takes a number input and will provide the month associated with that number'''
    n = int(n)
    if 1 <= n <= 12:
        month_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        number_month = n-1 # accounts for the 0th index
        return month_list[number_month]

    else: 
        print("Error in month_name, n=",n)
        return "XXX"
            
    
def main(): 
    file = open_file()
    print("Actual deaths (D) vs. Expected Deaths (E)")
    print("{:3s} ({:2s}) {:6s}".format("MTH", "WK", "Deaths"))
    
    for line in file:
        line = line.strip()
        line_list = line.split(",")
        
        if (line_list[0] == "United States") and (line_list[1] == "") and ("average" not in line_list[5]):
            num_deaths = int(line_list[8])
            num_ex_deaths = int(line_list[9]) 
            month = int(line_list[6])
            week = int(line_list[7])
            death_str = str_plot(month, week, num_deaths, "deaths") # want information on number of deaths
            ex_death_str = str_plot(month, week, num_ex_deaths, "expected") # want information on number of expected deaths
            print(death_str)
            print(ex_death_str)
            
            
if __name__ == '__main__':
    main() 

