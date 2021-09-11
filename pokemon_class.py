########################################################################################
#   ***Move Class ***
# 
#       Initializes a move for a Pokemon and allows for certain attributes to be returned 
#       to the users program as needed 
#
#   ***Pokemon Class***
#   
#       Initializes Pokemon granting certain attributes that can be used to interact with
#       that Pokemon and others. Allows for certain attributes to be returned to the users
#       program as needed
########################################################################################
from random import randint
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================
class Move(object): 
    def __init__(self, name="", element = "normal", power = 20, accuracy = 80, attack_type = 2):
        '''Initialize attributes of the Move object'''
        self.name = name
        self.element = element 
        self.power = power 
        self.accuracy = accuracy 
        self.attack_type = attack_type # attack type is 1, 2, or 3

    def __eq__(self, m): 
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()

    def __str__(self): 
        '''Returns a string in order to be printed'''
        return "{}".format(self.name)

    def __repr__(self): 
        '''References the __str__ method in order to represent/format the string'''
        return self.__str__() 

    def get_name(self):
        '''Returns the name of a move'''
        return self.name

    def get_element(self):
        '''Returns the element of a move'''
        return self.element

    def get_power(self): 
        '''Returns the power of a move'''
        return self.power

    def get_accuracy(self):
        '''Returns the accuracy of a move'''
        return self.accuracy 

    def get_attack_type(self): 
        '''Retruns the attack type of a move'''
        return self.attack_type

class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None, 
    hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        '''Initialize attributes of the Pokemon object'''
        self.name = name
        self.element1 = element1
        self.element2 = element2
        self.hp = hp
        self.patt = patt 
        self.pdef = pdef
        self.satt = satt 
        self.sdef = sdef
        self.moves = moves # how do you give this acces to a list of Moves

        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()
    
    def __str__(self): 
        '''Returns a string in order to be printed'''
        ret_str = ""
        ret_str += "{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}\n{:<15}{:<15}\n".format(self.name,self.hp, self.patt,self.pdef, self.satt, self.sdef,self.element1, self.element2)
        ret_str2 = ""
        for move in self.moves:
            ret_str2 += "{:<15}".format(str(move))
        return ret_str+ret_str2
                                                                            
    def __eq__(self, p): 
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __repr__(self): 
        '''References the __str__ method in order to represent/format the string'''
        return self.__str__()

    def get_name(self):
        '''Returns the name of a pokemon'''
        return self.name

    def get_element1(self): 
        '''Returns element 1 of a pokemon'''
        return self.element1

    def get_element2(self): 
        '''Returns element 2 of a pokemon'''
        return self.element2 

    def get_hp(self):
        '''Returns the hp of a pokemon'''
        return self.hp

    def get_patt(self):
        '''Returns the patt of a pokemon'''
        return self.patt

    def get_pdef(self):
        '''Returns the pdef of a pokemon'''
        return self.pdef

    def get_satt(self):
        '''Returns the satt of a pokemon'''
        return self.satt

    def get_sdef(self):
        '''Returns the sdef of a pokemon'''
        return self.sdef

    def get_moves(self):
        '''Returns the move of a pokemon'''
        return self.moves

    def get_number_moves(self):
        '''Returns the number of moves a pokemon has'''
        num = len(self.moves)
        return num
    
    def choose(self, index):
        '''takes an index and returns the corresponding move in the mves list'''
        try: 
            index_el = self.moves[index]
            return index_el
        except IndexError: # the index in beyond the moves list highest index
            return None

    def show_move_elements(self):
        '''Prints the elements that belong to each move of the pokemon'''
        ele_lst = []
        ele_str = ""
        for move in self.moves:
            move_el = move.get_element()    
            ele_lst.append(move_el)
        for element in ele_lst: 
            ele_str += "{:<15}".format(element)
        print(ele_str)

    def show_move_power(self):
        '''Prints the power of each respected move in the pokemon's moves list'''
        power_lst = []
        power_str = ""
        for move in self.moves:
            move_pow = move.get_power()    
            power_lst.append(move_pow)
        for power in power_lst: 
            power_str += "{:<15}".format(power)
        print(power_str)

    def show_move_accuracy(self):
        '''Prints the accuracy of each respected move in the pokemon's moves list'''
        acc_lst = []
        acc_str = ""
        for move in self.moves:
            move_acc = move.get_accuracy()    
            acc_lst.append(move_acc)
        for acc in acc_lst: 
            acc_str += "{:<15}".format(acc)
        print(acc_str)

    def add_move(self, move):
        '''Adds a move to the moves list of a pokemon, if list is less than 4'''
        if len(self.moves) < 4:
            self.moves.append(move)

    def attack(self, move, opponent):
        '''Attacks the opponent of a pokemon, calculates the damage that is inflicted onto the opponent'''
        mp = move.get_power()
        attack_type = move.get_attack_type()
        
        if attack_type == 2: 
            A = self.get_patt()
            D = opponent.get_pdef()
        elif attack_type == 3: 
            A = self.get_satt()
            D = opponent.get_sdef()
        else: 
            print("Invalid attack_type, turn skipped")
            return None 
    
        acc_value = randint(1,100)
        move_acc_value = move.get_accuracy()
        if acc_value > move_acc_value: 
            print('Move missed!')
            
        
        mod = 1.0
        opponent_ele_1 = opponent.get_element1()
        move_element = move.get_element()
        
        
        if opponent_ele_1 in is_effective_dictionary[move_element]:
            mod *= 2.0
        elif opponent_ele_1 in not_effective_dictionary[move_element]:
            mod *= 0.5 
        elif opponent_ele_1 in no_effect_dictionary[move_element]:
            mod *= 0 
        
        try:
            opponent_ele_2 = opponent.get_element2()
            #attacker_ele_2 = self.get_element()
            
            if opponent_ele_2 in is_effective_dictionary[move_element]:
                mod *= 2.0
            elif opponent_ele_2 in not_effective_dictionary[move_element]:
                mod *= 0.5 
            elif opponent_ele_2 in no_effect_dictionary[move_element]:
                mod *= 0
                
        except KeyError: 
            pass
            
        if mod > 1: 
            print("It's super effective!!!!")
        elif 0 < mod < 1: 
            print("Not very effective...")
        elif mod == 0: 
            print("No effect!")
            
        if self.element1 == move_element or self.element2 == move_element:
            mod *= 1.5
            
        damage = int(((( mp * (A/D) *20) / 50) + 2) * mod)
        opponent.subtract_hp(damage)
        
    def subtract_hp(self, damage):
        '''Subtracts the damage inflicted on a pokemon'''
        start_hp = self.get_hp()
        current_hp = start_hp - damage 
        if current_hp > 0: 
            self.hp = current_hp
        else: 
            self.hp = 0
        
        


