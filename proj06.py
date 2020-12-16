################################################################################
#   Computer Project #6
#   
#   Algorithm 
#   The user is prompted to input a file, if the file doesn't exist then ask for 
#   one that does. If the file exist then open said file, if they enter nothing
#   open "reactors-operating.csv". Display the menue options the user can choose
#   from. Options include: 
#       1.) # Reactors in each Reagion 
#       2.) Top energy producing reactors 
#       3.) Bottom energy producing reactors 
#       4.) List reactors in specidic state 
#       5.) Plot histogram for how long reactors have been active
#   Based on the option the user chose the approcpirate suite will run. Once an 
#   answer is printed the menu will display again and the user will be prompted 
#   for another option. This will continue until user inputs "Q" or "q".
################################################################################

import csv
import matplotlib.pyplot as plt

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def open_file():
    '''Will open a file, so long as the file exist'''
    answer = "continue"
    file_name = input('Please input a file to use: ') 
   
    while answer == "continue":
        try:
            if len(file_name) == 0: # if person hits enter 
                fp = open("reactors-operating.csv", "r", encoding="windows-1252") # opens the file in a way that I/computer can read 
            else:     
                fp = open(file_name, "r", encoding="windows-1252")
            return fp
            answer = "stop" 
    
        except FileNotFoundError: 
            print('Invalid filename, please try again')
            file_name = input('Please input a file to use: ')
            answer = "continue"
        
def read_file(fp):
    ''' Will read the file, ignoring the two header lines '''
    master_list = []
    reader = csv.reader(fp)
    next(reader,None)
    next(reader,None)
    for line in reader: 
        master_list.append(line)
    return master_list

def get_reactor_location(location_string):
    ''' Returns a simplified version of the location of the plant '''  
    location_list = location_string.split()
    new_location_list = [location_list[0]]
    for el in location_list[1:]:
        word = ""
        for cha in el:
            if (cha == "("): # get rid of extra info in () 
                break
            else:
                word += cha
                
        if word != "" and (")," not in word): # get rid of extra info in () and any blanck spaces
            new_location_list.append(word)
                
    if new_location_list[0].isalpha() and new_location_list[1] in STATES: 
        return ("{}, {}".format(new_location_list[0], new_location_list[1]))    
    
    elif new_location_list[0].isalpha() and not new_location_list[1].isalpha() and new_location_list[1] not in STATES: 
        return ("{} {} {}".format(new_location_list[0], new_location_list[1], new_location_list[2])) 
    
    elif new_location_list[0].isalpha() and new_location_list[1].isalpha and new_location_list[4] in STATES: 
        return ("{} {}, {}".format(new_location_list[0], new_location_list[1], new_location_list[2]))
           
    else: 
        return ("{} {}".format(new_location_list[0], new_location_list[1])) 

def reactors_per_region(master_list):
    ''' Counts and returns how many reactors in each region '''
    index = 0
    re_1_count = 0
    re_2_count = 0
    re_3_count = 0
    re_4_count = 0
    
    for l in master_list:
        reactor_region = int(master_list[index][5])
        if reactor_region == 1:
            re_1_count += 1
        elif reactor_region == 2:
            re_2_count += 1
        elif reactor_region == 3:
            re_3_count += 1
        else: 
            re_4_count += 1
            
        index += 1 
    return [re_1_count, re_2_count, re_3_count, re_4_count]

def top_react_by_mwt(master_list):
    ''' Returns which plants are in the top 10 based on MWt value '''
    index = 0
    list_of_tup = []
    new_list_of_tup = []
    for l in master_list:
        mwt = master_list[index][19]
        mwt = int(mwt)
        
        name_str = master_list[index][0]
        
        location_str = (master_list[index][4])
        location = get_reactor_location(location_str)
        
        list_of_tup.append((mwt, name_str, location)) #add formatting to the printing; not in the function
        index += 1 
    
    list_of_tup.sort(reverse=True)
    index = 0 
    while index < 10: # give top 10 plants
        new_list_of_tup.append(list_of_tup[index])
        index += 1
    return new_list_of_tup

def bot_react_by_mwt(master_list):
    ''' Returns which plants are in the bottom 10 based on MWt value '''
    index = 0
    list_of_tup = []
    new_list_of_tup = []
    for l in master_list:
        mwt = master_list[index][19]
        mwt = int(mwt)
        
        name_str = master_list[index][0]
        
        location_str = (master_list[index][4])
        location = get_reactor_location(location_str)
        
        list_of_tup.append((mwt, name_str, location))
        index += 1 
    
    list_of_tup.sort()
    index = 0 
    while index < 10: 
        new_list_of_tup.append(list_of_tup[index])
        index += 1
    return new_list_of_tup

def reactors_in_state (master_list, state):
    ''' Returns how many reactors are in the state provided, palnt names, and location'''
    index = 0
    re_in_state_tup = []
    for line in master_list:
        location = get_reactor_location(master_list[index][4])
        if location[-2:] == state: # checks last two characters which should be a state
            name_str = line[0]
            re_in_state_tup.append((name_str, location))
            index += 1
        else:
            index += 1
            continue
    if re_in_state_tup == []:
        return 0 
    
    return re_in_state_tup
    
def years_active (master_list):
    ''' Retruns how many years each plant was active in order from smallest to largest '''
    year_list = [int(line[32]) for line in master_list]   
    year_list.sort()    
    return year_list 

def plot_years_active(years_active_list):
    '''Given list of ints, plot histogram showing age of reactors in US'''
    plt.grid(which = 'both')
    plt.hist(years_active_list, bins=22, edgecolor='black')
    plt.title('Active years per Nuclear Reactor')
    plt.xlabel('Years active')
    plt.ylabel('Number of reactors')
    plt.show()

def display_options():
    '''Display menu of options for program'''
    OPTIONS = 'Menu\n\
1: # Reactors in each region\n\
2: Top energy producing reactors\n\
3: Bottom energy producing reactors\n\
4: List reactors in specific state\n\
5: Plot histogram for how long reactors have been active'       
    print(OPTIONS)
    return ""

def main():
    ''' Runs the appropriate suite based on the users answers '''
    file = open_file()
    master_list = read_file(file)  
    
    while True: 
        # for line in reader: 
        #     master_list.append(line)
        display_options()
        answer = input('Choose an option, q to quit: ')
        answer = answer.lower()
         
        
        if answer == "q":
            break 
        
        elif answer == "1":
            reactors = reactors_per_region(master_list)
            print("{:<8}{:<8}{:<8}{:<8}".format("NRC 1", "NRC 2", "NRC 3", "NRC 4"))
            print("{:<8}{:<8}{:<8}{:<8}".format(reactors[0], reactors[1], reactors[2], reactors[3]))
            
        
        elif answer == "2":
            top_mwt_list = top_react_by_mwt(master_list)
            print('\nTop 10 Reactors by MWt')
            print('{:<8}{:<30}{:<10}'.format("MWt", "Reactor Name", "Location"))
            for tup in top_mwt_list:  
                print('{:<8}{:<30}{:<10}'.format(tup[0], tup[1][0:25], tup[2])) # [0:26] will slice the string for better printing 
            
        
        elif answer == "3": 
            top_mwt_list = bot_react_by_mwt(master_list)
            print('\nBottom 10 Reactors by MWt')
            print('{:<8}{:<30}{:<10}'.format("MWt", "Reactor Name", "Location"))
            for tup in top_mwt_list:  
                print('{:<8}{:<30}{:<10}'.format(tup[0], tup[1][0:25], tup[2]))
            
        
        elif answer == "4":
            state = input('Please enter a 2 letter state code: ')
            state = state.upper()
            state_answer = True 
            
            while state_answer == True:
                if state in STATES: 
                    re_in_state = reactors_in_state(master_list, state)
                    state_answer = False 
                
                else: 
                    print('Please input a valid state')
                    state = input('Please enter a 2 letter state code: ')
                    state = state.upper()
                    state_answer = True
                    continue 
                
            if re_in_state == 0:
                print('\nThere are 0 reactors in {}'.format(state))
            else: 
                plant_count = 0 
                for ele in re_in_state: 
                    plant_count += 1
                    
                print('\nThere are {} reactors in {}:'.format(plant_count, state))
                for ele in re_in_state: 
                    print("{} in {}".format(ele[0],ele[1]))

                    
        elif answer == "5":
            years = years_active(master_list)
            plot_years_active(years) 
            
        else: 
            print('\nInvalid choice, please try again')
            
if __name__ == '__main__':
    main()