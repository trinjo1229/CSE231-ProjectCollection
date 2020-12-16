################################################################################
#   Computer Project #9 
#
#   Algorithm 
#       The user is asked to provide two years that are seperated by a sinlge 
#       comma. The program will the then open the appropriate file based on the 
#       years provided. The user is then asked to choose from one of the opntions
#       provided inclduing: 
#           1. Search by Country
#           2. Top 10 Countries 
#           3. Compare Countries 
#           x. Exit
#       Based of the option that the user chose, the appropriate suite will run.
#       The user will continue to be asked what option they'd like to run, that 
#       is until they enter "x" or "X", at this point the program will stop.
################################################################################

import csv
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt

def open_file(year_str):
    ''' Opens a file based on the year provided '''
    try: 
        fp = open(year_str + ".csv", "r")
        return fp
    except FileNotFoundError: 
        return None

def build_dictionary(fp): 
    ''' Builds a dictionary based on the contents of the file provided '''
    reader = csv.reader(fp)
    next(reader, None)
    outter_d = {}
    for line in reader: 
       if "N/A" not in line: 
           country = line[0]
           region = line[1]
           inner_d_tup = ((int(line[2]), float(line[3])), (float(line[5]), float(line[9])), (float(line[6]), float(line[7]), float(line[8])))
           if region not in outter_d: 
               outter_d[region] = {}
   
           outter_d[region][country] = inner_d_tup
           
    return (outter_d)

def combine_dictionaries(year, subD, superD):
    ''' Adds a dictionary as a value to the key of an outer dictionary '''
    superD[year] = subD
    return superD

def search_by_country(country, superD, print_boolean):
    ''' Searches for the country provided, print the data on that country from 2 years will print results if prompted '''
    temp_results_list = []
    super_keys = list(superD.keys())
    super_values = superD.values()  
    for region in super_values: # goes into the dictionary of each year in order to reach the country keys and values
        for coun in region: 
            region_values = region.values()
            for ele in region_values: 
                if country in ele: 
                    temp_results_list.append(ele[country])
                    break
            break
    
    year1_results_tup = (temp_results_list[0][0][1], temp_results_list[0][2][0], temp_results_list[0][2][1], temp_results_list[0][2][2])
    year2_results_tup = (temp_results_list[1][0][1], temp_results_list[1][2][0], temp_results_list[1][2][1], temp_results_list[1][2][2])
    
    year1 = super_keys[0] 
    year2 = super_keys[1]
    year1_rank, year2_rank = temp_results_list[0][0][0], temp_results_list[1][0][0]
    year1_score, year2_score = temp_results_list[0][0][1], temp_results_list[1][0][1]
    year1_family, year2_family = temp_results_list[0][2][0], temp_results_list[1][2][0]
    year1_health, year2_health = temp_results_list[0][2][1], temp_results_list[1][2][1]
    year1_freedom, year2_freedom = temp_results_list[0][2][2], temp_results_list[1][2][2]
    
    if print_boolean == True: 
        print('{:<10s}{:<s}'.format("Year:", year1))
        print('{:<10s}{:<s}'.format("Country:", country))
        print('{:<10s}{:<5d}'.format("Rank:", year1_rank))
        print('{:<10s}{:<5.2f}'.format("Score:", year1_score))
        print('{:<10s}{:<5.2f}'.format("Family:", year1_family))
        print('{:<10s}{:<5.2f}'.format("Health:", year1_health))
        print('{:<10s}{:<5.2f}'.format("Freedom:", year1_freedom))
        print('-'*20)
        
        print('{:<10s}{:<s}'.format("Year:", year2))
        print('{:<10s}{:<s}'.format("Country:", country))
        print('{:<10s}{:<5d}'.format("Rank:", year2_rank))
        print('{:<10s}{:<5.2f}'.format("Score:", year2_score))
        print('{:<10s}{:<5.2f}'.format("Family:", year2_family))
        print('{:<10s}{:<5.2f}'.format("Health:", year2_health))
        print('{:<10s}{:<5.2f}'.format("Freedom:", year2_freedom))
        print('-'*20)
    else: 
        return [year1_results_tup, year2_results_tup] 

def top_10_ranks_across_years(superD, year1, year2):
    ''' Prints the top twen countreis from year one, compares those reults with the second year '''
    year1_countries_list = [] # will not be sorted
    year2_countries_list = []
    
    for region in superD[year1]: 
       for country in superD[year1][region]:
           tup = superD[year1][region][country]
           country_tup = (country, tup[0][0])
           year1_countries_list.append(country_tup)
                         
    sorted_year1_countries_list = sorted(year1_countries_list, key=itemgetter(1)) #sorts based on the rank of the country

    for ele in sorted_year1_countries_list: # make a list that compares the same countries but form the second year
        for region in superD[year1]: 
            for country in superD[year2][region]:
               if country == ele[0]: 
                   tup = superD[year2][region][country]
                   country_tup = (country, tup[0][0])
                   year2_countries_list.append(country_tup)
    
    top_10_year1 = sorted_year1_countries_list[0:10] # only lookib=ng for the top ten countries 
    top_10_year2 = year2_countries_list[0:10]
    
    return (top_10_year1),(top_10_year2)
def print_ranks(superD, list1, list2, year1, year2):
    ''' Prints the rankings found from the top_20_ranks_across_years function '''
    year1_happ_rank_lst = [] # not sorted
    year2_happ_rank_lst = []
    average_happ_lst = []
    
    for region in superD[year1]: 
       for country in superD[year1][region]:
           for tup in list1: 
               if tup[0] == country:
                   tup = superD[year1][region][country]
                   country_tup = (country, tup[0])
                   year1_happ_rank_lst.append(country_tup)
                   
    sorted_year1_happ_rank_lst = sorted(year1_happ_rank_lst, key=itemgetter(1))
    
    for ele in sorted_year1_happ_rank_lst: 
        for region in superD[year1]: 
            for country in superD[year2][region]:
               if country == ele[0]: 
                   tup = superD[year2][region][country]
                   country_tup = (country, tup[0])
                   year2_happ_rank_lst.append(country_tup)

    count1 = 0
    for tup in sorted_year1_happ_rank_lst: 
        average = (tup[1][1] + year2_happ_rank_lst[count1][1][1]) / 2
        average_happ_lst.append(average)
        count1 += 1
    
    print("{:<15s} {:>7s} {:>7s} {:>12s}".format("Country", year1, year2, "Avg.H.Score"))
    count2 = 0 
    for tup in sorted_year1_happ_rank_lst: 
        print("{:<15s} {:>7d} {:>7d} {:>12.2f}".format(tup[0], tup[1][0], list2[count2][1], average_happ_lst[count2]))
        count2 += 1
        
def prepare_plot(country1, country2, superD):
    ''' Creates and returns tuples with information on the two countries provided '''
    while True: 
        try:
            country1_search = search_by_country(country1, superD, False)
            country2_search = search_by_country(country2, superD, False)
            return country1_search[0], country2_search[0]  
        except IndexError: 
            print("Invalid input. Try again.")  
            return None             

def bar_plot(country1, country2, countrylist1, countrylist2):
    ''' Bar plot comparing two countries.'''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    N = 4
    ind = np.arange(N)
    width = 0.25

    rects1 = ax.bar(ind, countrylist1, width,
                    color='black',
                    error_kw=dict(elinewidth=2, ecolor='blue'))

    rects2 = ax.bar(ind + width, countrylist2, width,
                    color='red',
                    error_kw=dict(elinewidth=2, ecolor='red'))

    ax.set_xlim(-width, len(ind) + width)
    ax.set_ylabel('Quantity')
    ax.set_title('Comparison between the two countries')
    xTickMarks = ['Happiness Sc.', 'Family', 'Health', 'Freedom']
    ax.set_xticks(ind + width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=0, fontsize=10)

    ax.legend((rects1[0], rects2[0]), (country1, country2))
    plt.show()

def main():
    ''' Docstring '''

    BANNER = '''
                    __ooooooooo__
                 oOOOOOOOOOOOOOOOOOOOOOo
             oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
          oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
        oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
      oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
     oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
    oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
    oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
    oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
    oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
    oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
    *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
    *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
     *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
      *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
        *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
          *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*      
             *OOOOOOOOo           oOOOOOOOO*      
                 *OOOOOOOOOOOOOOOOOOOOO*    
                      ""ooooooooo""
    '''

    MENU = '''
    1. Search by country
    2. Top 10 countries
    3. Compare countries
    x. Exit 
    :'''
    print(BANNER)

    superD = {}

    while True:

        file_answer = input("Input Years comma-separated as A,B: ")
        file_answer_lst = file_answer.split(",")
        if len(file_answer_lst) == 1: 
            print("Input Error: enter two years, comma-separated.")
            continue
        year_1 = file_answer_lst[0]
        year_2 = file_answer_lst[1]
        fp1 = open_file(year_1)
        fp2 = open_file(year_2)
        
        if fp1 != None or fp2 != None:
            break
        else: 
            print('Invalid filename')
            continue 
    print("Opening Data file for year {}: ".format(year_1))
    print("Opening Data file for year {}: ".format(year_2))
    dictionary1 = build_dictionary(fp1)
    dictionary2 = build_dictionary(fp2)
    
    year1_main_dictionary = combine_dictionaries(year_1, dictionary1, superD)    
    year2_main_dictionary = combine_dictionaries(year_2, dictionary2, superD)  
    
    
    fp1.close()
    fp2.close()
    user_choice = input(MENU)
    
    while user_choice.lower() != 'x':
        
        
         if user_choice == "1": 
             country = input("[ ? ] Please specify the country: ")
             boolean = True
             search_resultss = search_by_country(country, superD, boolean)
         
         elif user_choice == "2": 
             results = top_10_ranks_across_years(superD, year_1, year_2)
             print_results = print_ranks(superD, results[0], results[1], year_1, year_2)
         
         elif user_choice == "3": 
             while True: 
                 country_input = input("[ ? ] Please specify the two countries (A,B): ")
                 countries = country_input.split(",")
                 
                 if len(countries) == 2:
                     plot_prep = prepare_plot(countries[0], countries[1], superD)
                     
                     if plot_prep == None: 
                        continue
                     
                     else:
                         print("{:<20s} {:<9s} {:<8s} {:<8s} {:<8s}".format("\nCountry","Hap.Score","Family","Life Ex.","Freedom"))
                         
                         print("{:<20s} {:<9.2f} {:<8.2f} {:<8.2f} {:<8.2f}".format(countries[0], plot_prep[0][0],\
                         plot_prep[0][1], plot_prep[0][2], plot_prep[0][3]))
                         
                         print("{:<20s} {:<9.2f} {:<8.2f} {:<8.2f} {:<8.2f}".format(countries[1], plot_prep[1][0],\
                         plot_prep[1][1], plot_prep[1][2], plot_prep[1][3])) 
                         plot_answer = input("[ ? ] Plot (y/n)? ").lower()    
                        
                         if plot_answer == "y":
                             bar_plot(countries[0], countries[1], plot_prep[0], plot_prep[1])
                             break
                         
                         else: 
                             break
                     
                 else: 
                     print("[ - ] Incorrect input. Try again.")
                     continue 
                 
         else:
            print("[ - ] Incorrect input. Try again.")
         user_choice = input(MENU)

if __name__ == '__main__':
    main()