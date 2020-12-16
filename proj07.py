################################################################################
#   Computer Project #7 
#   
#   Algorithm
#       The user is promted for a csv file to be opened. If it can be opened 
#       Then the file is read through, and a master list of the data is created. 
#       The user is then given a menue of options including: 
#           1. Visualize damage data for a single year
#           2. Visualize earthquakes magnitudes for a single year
#           3. Visualize number of earthquake and their damages within a range 
#              of years
#           4. Exit the program 
#       Based on the option that the user chose the approriate suite will run 
#       and the data that has been gathered on the earthquakes will be used. 
#       The user will also be asked if they'd like a graph, if they do then 
#       a graph will be provided based on their search. This program will 
#       continue to run until the user decided the exit. 
################################################################################

import pylab as py
import csv

MONTHS = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

def open_file():
    '''Will open a file, so long as the file exist'''
    answer = "continue"
    file_name = input("Enter filename: ") 
    while answer == "continue":
        try:
            file = open(file_name, "r")
            file.readline()
            return file
            answer = "stop" 
    
        except FileNotFoundError: 
            print("\nFile is not found! Please Try Again!")
            file_name = input("Enter filename: ")
            answer = "continue"    

def read_file(fp):
    '''reads through the csv file docuenting important data, if this data can be \
        turned into a float or int then that row is skipped'''
    master_list = []
    reader = csv.reader(fp)
    for line in reader:
        try: 
            year = int(line[2])
            month = int(line[3])
            magnitude = float(line[9])
            location = line[19]   
            latitude = float(line[20])
            longitude = float(line[21])
            
            deaths = line[23]
            if deaths == "": 
                deaths = 0
            else: 
                deaths = int(deaths)
            
            missing = line[25]
            if missing == "": 
                missing = 0    
            else: 
                missing = int(missing)
             
            injuries = line[27]
            if injuries == "": 
                injuries = 0 
            else: 
                injuries = int(injuries)
            
            damages = line[29] 
            if damages == "": 
                damages = 0
            else: 
                damages = float(damages)
             
            tup = (year, month, magnitude, location, latitude, longitude, deaths, missing, injuries, damages)
            master_list.append(tup)
        except ValueError:
            continue    
    return sorted(master_list)  

def get_damage_data(data, year):
    '''gathers the all casualties from earthquakes that happened in every month of that year'''
    damage_data_list = []
    for tup in data:
        if tup[0] == year: 
            month = tup[1]
            location = tup[3][0:40] # print limited characters for better display 
            deaths = tup[6]
            missing = tup[7]
            injuries = tup[8]
            damages = tup[9]
            
            data_tup = (month, location, deaths, missing, injuries, damages)
            damage_data_list.append(data_tup)
        
    if damage_data_list == []:
        return []
    else: 
        return damage_data_list
    
def get_quake_data(data, year):
    '''gathers information on the earthquakes themselves that happened in a select year'''
    quake_data_list = []
    for tup in data:
        if tup[0] == year: 
            month = tup[1]
            magnitude = tup[2]
            location = tup[3]
            latitude = tup[4]
            longitude = tup[5]
            
            data_tup = (month, magnitude, location, latitude, longitude)
            quake_data_list.append(data_tup)
           
    if quake_data_list == []:
        return []
    else: 
        return quake_data_list    

def summary_statistics(data, year_start, year_end):
    '''sumarizes how many earthquakes happened in that time frame, \ 
    how much they cost, and the casualties associated with them'''
    earthquake_count_by_year = []
    total_damages_by_year = []
    casualties_by_year = [] 
    
    if not year_start <= year_end: 
        return [earthquake_count_by_year, total_damages_by_year, casualties_by_year]
    
    for year in range(year_start,year_end+1):
        num_quake_data = get_damage_data(data, year)
        num_of_quakes = len(num_quake_data) # counts the number of earthquakes that happened
        tup = (year, num_of_quakes)
        earthquake_count_by_year.append(tup)
    
        damages_from_quake = get_damage_data(data, year) #list of tuples
        total_damages_per_year = 0
        for el in damages_from_quake:
            total_damages_per_year += el[-1] 
        
        tup = (year, total_damages_per_year)
        total_damages_by_year.append(tup)
        
        
        num_of_casualties = get_damage_data(data, year)
        total_deaths = 0 
        total_missing = 0 
        total_injured = 0 
        for el in num_of_casualties: 
           total_deaths += el[2] 
           total_missing += el[3] 
           total_injured += el[4] 
    
        tup = (year, (total_deaths, total_missing, total_injured))
        casualties_by_year.append(tup)
        
    return_list = [earthquake_count_by_year, total_damages_by_year, casualties_by_year]
    
    # if all the years in the list come back with zeros then return nothing    
    if return_list[0][-1][-1] == 0 and return_list[1][-1][-1] == 0 and \
    return_list[2][-1][-1][0] == 0 and return_list[2][-1][-1][1] == 0 and return_list[2][-1][-1][2] == 0: 
        return "nothing"

    return [earthquake_count_by_year, total_damages_by_year, casualties_by_year]
             
        
def display_damage_data(L, year):
    '''displays the data gathered from get_damage_data function'''
    if L == []:
        print("\nYear input '{}' is incorrect!".format(year))
        return "nothing"     
    else: 
        header_1 = "Earthquake damage costs in {}".format(year)
        print("{:^98}".format(header_1))
        print("{:8s}{:40s}{:>12s}{:>12s}{:>12s}{:>14s}".format("Month","Location","Deaths","Missing","Injuries","Damage"))
        print("{:8s}{:40s}{:>12s}{:>12s}{:>12s}{:>14s}".format("","","","","","(Millions)"))
        
        total_deaths = 0 
        total_missing = 0 
        total_injuries = 0 
        total_damages = 0
        
        for tup in L: 
            month = MONTHS[(tup[0] - 1)]
            location = tup[1]
            
            deaths = tup[2]
            total_deaths += deaths
            
            missing = tup[3]
            total_missing += missing 
            
            injuries = tup[4]
            total_injuries += injuries 
            
            damages = tup[5]
            total_damages += damages 
            
            print("{:<8s}{:40s}{:12,d}{:12,d}{:12,d}{:14,.2f}".format(month, location, deaths, missing, injuries, damages))
        print("{:<8s}{:40s}{:12,d}{:12,d}{:12,d}{:14,.2f}".format("Total","", total_deaths, total_missing, total_injuries, total_damages))        
        
def display_quake_data(L, year):
    '''displays data form the _get_quake_data function'''
    if L == []:
        print("\nYear input '{}' is incorrect!".format(year))
        return "nothing" 
    else: 
        header1 = "Earthquake magnitudes and locations in {}".format(year)
        print("{:^58}".format(header1))
        print("{:8s}{:10s}{:40s}".format("Month","Magnitude","Location"))
        
        for tup in L: 
            month = MONTHS[(tup[0]-1)]
            magnitude = tup[1]
            location = tup[2]
            print("{:<8s}{:<10.2f}{:40s}".format(month, magnitude, location))
        

def display_summary(quakes, costs, casualties):
    '''displays the data gathered from summary_statistics function'''
    grand_total_quakes = 0 
    grand_total_costs = 0  
    grand_total_dead = 0 
    grand_total_missing = 0 
    grand_total_injured = 0 
    temp_lst1 = []
    temp_lst2 = []
    
    if quakes == [] and costs == [] and casualties == []: 
        return "nothing" 
    
    print("\nNumber of earthquakes and costs per year")
    print("{:5s}{:>10s}{:>12s}".format("Year", "Quakes", "Cost"))
   
    
    for num,cost in zip(quakes, costs): 
        year = num[0]
        num_of_quakes = num[1]
        grand_total_quakes += num_of_quakes
        total_cost = cost[1]
        grand_total_costs += total_cost
        temp_tup = (year, num_of_quakes, total_cost)
        temp_lst1.append(temp_tup)
        
    for el in temp_lst1: 
        print("{:<5d}{:10,d}{:12,.2f}".format(el[0], el[1], el[2]))
    
    print("{:<5s}{:10,d}{:12,.2f}".format("Total", grand_total_quakes, grand_total_costs))
    print()
    print("\nTotal Casualties")
    print("{:10s}{:>10s}{:>11s}".format("Casualties", "Total", "Percent"))   
    
    
    for el in quakes: 
        grand_total_quakes += el[1]
    for el in costs: 
        grand_total_costs += el[1]
    for el in casualties: 
        grand_total_dead += el[1][0] 
        grand_total_missing += el[1][1] 
        grand_total_injured += el[1][2]
    
    grand_total_casulaties = grand_total_dead + grand_total_missing + grand_total_injured
    death_percent = (grand_total_dead / grand_total_casulaties) * 100  # allows for the percent to be out of 100
    missing_percent = (grand_total_missing / grand_total_casulaties) * 100
    injured_percent = (grand_total_injured / grand_total_casulaties) * 100
    
    death_tup = ("Deaths", grand_total_dead, death_percent)
    temp_lst2.append(death_tup)
    missing_tup = ("Missing", grand_total_missing, missing_percent)
    temp_lst2.append(missing_tup)
    injured_tup = ("Injured", grand_total_injured, injured_percent)
    temp_lst2.append(injured_tup)
    
    for el in temp_lst2:
        print("{:10s}{:10d}{:10,.2f}%".format(el[0], el[1], el[2]))
        
def plot_intensity_map(year, quake_data):
    '''
        This function plots the map of the earthquake locations for the
        selected year. This function is provided in the skeleton code.
        
        Parameters:
            year (string): The year key for the data to plot
            size (int): Number of earthquakes that occured in the selected year
            
            coordinates (list): List of (latitude,longitude) coordinates for
                                the trajectory of each earthquake that occured
                                in the selected year.
                                
        Returns: None
    '''
    
    
    # The the RGB list of the background image.
    img = py.imread("world-map.jpg")

    # Set the max values for the latitude and longitude of the map
    max_longitude, max_latitude = 180, 90
    
    # Set the background image on the plot
    py.imshow(img,extent=[-max_longitude,max_longitude,\
                          -max_latitude,max_latitude])
    
    
    # Show the atlantic ocean region
    py.xlim((-max_longitude,max_longitude))
    py.ylim((-max_latitude,max_latitude))
    
    
    # build the x,y coordinates map
    lst = list(zip(*quake_data))
    lat,lon,mag = lst[3],lst[4],lst[1] 
    
    area = ([(1.0 * p) ** 2 for p in mag ])
    
    
    # plot the scatter plot
    scatter = py.scatter(lon,lat,s=area, c=mag, cmap='seismic')    
    py.colorbar(scatter)
    
    # Set the labels and titles of the plot
    py.xlabel("Longitude (degrees)")
    py.ylabel("Latitude (degrees)")
    py.title("Earthquake Magnitude points for {}".format(year))
    py.show() # show the full map

def plot_bar(L, title, x_label, y_label):
    '''
        This function receives a list of x,y values.
        
        Parameters
            L (list): 
            title (str):
            x_label (str):
            y_label (str):
                
        Returns
            None
    '''
    
    #count the earthquakes per month
    total = [0]*12
    for i in L:
        total[i[0]-1] += 1
    
    
    py.title(title)
    py.xlabel(x_label)
    py.ylabel(y_label)
    py.xticks(range(12),MONTHS)
    py.bar(range(12), total)
    py.show()

def plot_line(L, title, x_label, y_label):
    '''
        This function receives a list of x,y values.
        
        Parameters
            L (list): 
            title (str):
            x_label (str):
            y_label (str):
        
        Returns
            None
    '''
    res = list(zip(*L))
    
    py.title(title)
    py.xlabel(x_label)
    py.ylabel(y_label)
    py.xticks(range(len(res[0])),[str(r) for r in res[0]], rotation=90)
    py.plot(range(len(res[0])),res[1], marker="o")
    
    py.show()

def plot_pie(L, title):
    '''
        This function receives a list of x,y values.
        
        Parameters
            L (list): 
            title (str):
                
        Returns
            None
    '''
    #            L[2].append((y,(deaths,missing,injured)))
    deaths = sum([t[0] for y,t in L])
    missing = sum([t[1] for y,t in L])
    injured = sum([t[2] for y,t in L])
    total = deaths + missing + injured
    d = deaths/total
    m = missing/total
    i = injured/total
    L = [["deaths",d],["missing",m],["injuries",i]]

    res = list(zip(*L))
    
    py.title(title)
    py.pie(res[1],labels=res[0],autopct='%.1f%%') 
    py.show()

    
def main():    
    '''
        This program will show damages caused by an earthquakes in a year.
        Also, it will plot the intensity of all earthquakes observed in a year.
    
    '''
    
    MENU = '''\nEarthquake data software
        
        1) Visualize damage data for a single year
        2) Visualize earthquakes magnitudes for a single year
        3) Visualize number of earthquake and their damages within a range of years
        4) Exit the program
    
        Enter a command: '''
    
    file = open_file()
    master_list = read_file(file)
    
    while True: 
        answer = input(MENU)
        
        if answer == "4":
            break
        
        elif answer == "1":
            year = input("Enter a year: ")
            try: 
                year = int(year)
            except: 
                print("\nYear input '{}' is incorrect!".format(year))
                continue
            
            year = int(year)
            data = get_damage_data(master_list, year)
            display_data = display_damage_data(data, year) 
            
            if display_data == "nothing":
                continue
             
            else:
                plot_answer = input("Do you want to plot (y/n)? ")
                plot_answer = plot_answer.lower()
                if plot_answer == "y":
                    title = "Monthly earthquakes in {}".format(year)
                    plot_bar(data, title, "months", "earthquakes")  
            
        elif answer == "2":
            year = input("Enter year: ")
            try: 
                year = int(year)
            except: 
                print("\nYear input '{}' is incorrect!".format(year))
                year = "invalid"
                continue
            
            year = int(year)
            data = get_quake_data(master_list, year)
            display_data = display_quake_data(data, year)
            
            if display_data == "nothing": 
                continue 
            else: 
                plot_answer = input("Do you want to plot (y/n)? ")
                plot_answer = plot_answer.lower()
                if plot_answer == "y":
                    plot_intensity_map(year, data) 
                
        elif answer == "3": 
            s_year = input("Enter start year: ")
            e_year = input("Enter end year: ")
            
            try: 
                s_year = int(s_year) 
                e_year = int(e_year)
            except ValueError: 
                print("\nYear range [{},{}] is invalid!".format(s_year, e_year))
                
            L = summary_statistics(master_list, s_year, e_year)
            if L == "nothing":
                print("\nYear range [{},{}] is invalid!".format(s_year, e_year))
                continue 
            else: 
                display_data = display_summary(L[0], L[1], L[2])
            
            if display_data == "nothing":
                continue 
            else: 
                plot_answer = input("Do you want to plot (y/n)? ")
                plot_answer = plot_answer.lower()
                if plot_answer == "y":
                    earthquake_title = "Total earthquakes between {} and {}".format(s_year, e_year)
                    casualty_title = "Total casaulties caused by earthquakes between {} and {}".format(s_year, e_year)
                    cost_title = "Total costs caused by earthquakes between {} and {}".format(s_year, e_year)
                    
                    plot_line(L[0], earthquake_title, "Year", "Earthquakes") 
                    plot_line(L[1], cost_title, "Year", "Costs")
                    plot_pie(L[2], casualty_title)
        
        else: 
            print("\nOption '{}' is invalid! Please Try Again!".format(answer))
            
             
    print("\nThank you for using this program!")


if __name__ == "__main__":
    main()
