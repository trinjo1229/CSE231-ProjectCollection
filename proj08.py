###############################################################################
#   Computer Project #8
#
#   Algorithm 
#   The user is prompted to input a file, if the file doesn't exist then they're
#   promted to put in one that does. If they enter an empty space then FOOD.txt
#   is opened automatically. A list of food and a list of the minerals that will
#   be considered are printed. The user is then promted to give three elememts 
#   that are seperated by "&" or "|". If the input is correct then the foods 
#   that fit the restrictions set by the user are printed. The user is then 
#   promted for another input. This will continue until the user enters "Q" or 
#   "q". At this point the program will print foods that are recommended for 
#   those who are anemic and then stop. 
###############################################################################
import csv

def open_file():
    '''Opens a file so long as it exist'''
    answer = "continue"
    file_name = input('Please input a file to use: ') 
   
    while answer == "continue":
        try:
            if len(file_name) == 0: # if person hits enter 
                fp = open("FOOD.txt", "r") 
            else:     
                fp = open(file_name, "r")
            return fp
            answer = "stop" 
    
        except FileNotFoundError: 
            print("Invalid filename, please try again")
            file_name = input('Please input a file to use: ')
            answer = "continue"  

def read_file(fp):
    '''Reads the file and reterns a Dictionary of the file read'''
    minerals_D = {}
    reader = csv.reader(fp)
    for line in reader: 
        build_dictionary(minerals_D, line)
     
    return minerals_D  


def food_and_minerals(D):
    '''Creates two seperate list one for food, the other for minerals'''
    minerals_list = []
    food_list = []
    minerals_set = set()
    food_set = set()
    
    for mineral in D.keys():
        minerals_set.add(mineral)
    
    for values in D.values(): 
        for food in values: 
            food_set.add(food)
    
    for mineral in minerals_set:  
        minerals_list.append(mineral)
        
    for food in food_set: 
        food_list.append(food)
    
    minerals_list = sorted(minerals_list)
    food_list = sorted(food_list)
    return food_list, minerals_list

def build_dictionary(D,line_list):
    '''Builds a dictionary based on the lines provided from a file'''
    # D is a dictionary that has elements for keys
    for el in line_list[1:]: 
        if el not in D: 
            D[el] = {line_list[0]}
        else:
            D[el].add(line_list[0])

def search(minerals_str,minerals_list,D):
    '''Searches for foods based on the 3 elements the user has provided'''
    food_set = set()
    minerals_prov_lst = []
    mineral_count = 0
    operator_sign = ""
    
    minerals_str = minerals_str.lower()
    if not minerals_str.isalpha(): # are the operations present 
        find_first_op_loc = minerals_str.find("&")
        
        if find_first_op_loc == -1: # "&" wasn't used, assume "|" was used
            minerals_prov = minerals_str.split("|")
            operator_sign = "|"
            for ele in minerals_prov: 
                ele = ele.strip()
                minerals_prov_lst.append(ele)
        else: 
            find_second_op_loc = minerals_str.rfind("&")
            if find_first_op_loc == find_second_op_loc: # 2 operations were used or "&" was used only once
                return None
            else: 
                minerals_prov = minerals_str.split("&")
                operator_sign = "&"
                for ele in minerals_prov: 
                    ele = ele.strip()
                    minerals_prov_lst.append(ele)
        
    elif minerals_str == "q": 
        return "Stop"
   
    else: 
        return None
    
    for ele in minerals_prov_lst: 
        if ele in minerals_list: 
            mineral_count += 1
            
    if mineral_count == 3:
    
        if operator_sign == "&":
            first_min = minerals_prov_lst[0]
            second_min = minerals_prov_lst[1]
            third_min = minerals_prov_lst[2]
            first_food_set = D[first_min] 
            second_food_set = D[second_min]
            third_food_set = D[third_min]
            combined_set = first_food_set & second_food_set & third_food_set
            
            for ele in combined_set: 
                food_set.add(ele)
                
            return food_set
        
        else: 
            items = D.items()
            for tup in items: 
                if tup[0] in minerals_prov_lst: 
                    for ele in tup[1]: 
                        food_set.add(ele)
                        
            return food_set
        
    else: 
        return None
    
def anti_anemia(D):
    '''Creates a list of foods that have iron in them'''
    return D["iron"]
    

def main():
    '''Provides food results based on the users input, so long as the input if valid'''
    file = open_file()
    dictionary = read_file(file)
    food_and_minerals_list = food_and_minerals(dictionary)
    
    print("We consider these foods:")
    for ele in sorted(food_and_minerals_list[0]): 
        print(ele)
        
    print()
    print("We consider these minerals:")
    
    for ele in sorted(food_and_minerals_list[1]): 
        print(ele)
        
    while True: 
        print("\nSpecify three types of minerals separated by &(and) or |(or)")
        minerals_str = input("Please enter 3 minerals using a single operand type (or q to quit): ")
        
        foods_found = search(minerals_str, food_and_minerals_list[1], dictionary)
        
        if foods_found == None: 
            print("Error in input.")
            
        elif foods_found == "Stop": 
            print("Foods that contain iron, please eat these foods if you are anemic: ")
            iron_food = anti_anemia(dictionary)
            
            for ele in sorted(iron_food): 
                if ele != sorted(iron_food)[-1]:
                    print(ele, end=", ")
                else: 
                    print(ele, end="")
            break 
        
        else: 
            for ele in sorted(foods_found): 
                print(ele)
            
        
        
if __name__ == "__main__":
    main()