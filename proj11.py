################################################################################
#   Computer Project #11
#
#      Algorithm 
#      The program will open a pokemon file and a move file and read through 
#      them creating a master list of pokemon and moves respectively. The two 
#      users will then be asked to pick a pokemon by name or by index. If it 
#      can't be found then the users will be promted to enter another option. 
#      After each player choses an pokemon it'll be display that pokemon and 
#      it's elements. After the user has chosen their pokemon the program will 
#      add 4 moves to the pokemon. From that point the two users will be able to
#      combat. The round will continue until one of the players quit or until one
#      of the players dies, at that point the program will ask if they'd like 
#      to contnue. If they do then the game will restart if not a goodbye message
#      is printed and the game will stop. 
################################################################################

import csv
from random import randint 
from random import seed 
from copy import deepcopy
from pokemon import Pokemon 
from pokemon import Move
seed(1)

# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================

def read_file_moves(fp): 
    '''blah'''
    moves_list = []
    
    reader = csv.reader(fp)
    next(reader, None)
    for line in reader:
        if line[2] == "1":
            if line[9] != "1":
                if line[4] != "":
                    if line[6] != "":
                        name = line[1]
                        element = element_id_list[int(line[3])]
                        power = int(line[4])
                        accuracy = int(line[6])
                        attack_type = int(line[9])
                        move_instance = Move(name, element, power, accuracy, attack_type)
                        moves_list.append(move_instance)
                    else: 
                        continue # no accuracy value
                else: 
                    continue # no power value
            else: 
                continue # if attack_type is not 1
        else:
            continue # if generation_id is not 1 
        
    return moves_list
    

def read_file_pokemon(fp):
    '''Reads through a csv file of pokemon, will skip those that are not first \ 
    gen and those that have the same index and a pokemon alreadt added'''
    pokemon_list = []
    pokemon_id_set = set()
    
    reader = csv.reader(fp)
    next(reader, None)
    for line in reader: 
        if line[11] == "1": 
            if line[0] not in pokemon_id_set: 
                name = line[1].lower()
                element1 = line[2].lower()
                element2 = line[3].lower()
                moves = None
                hp = int(line[5])
                patt = int(line[6])
                pdef = int(line[7])
                satt = int(line[8])
                sdef = int(line[9])
                pokemon_instance = Pokemon(name, element1, element2, moves, hp, patt, pdef, satt, sdef)
                pokemon_list.append(pokemon_instance)
                pokemon_id_set.add(line[0])
            else:
                continue # already checked this id_#
        else: 
            continue # generation isn't 1
    return pokemon_list    
 
def choose_pokemon(choice, pokemon_list):
    '''Finds the pokemon of the user's chosing based on name or by an index'''
    if choice.isalpha(): 
        choice = choice.lower()
        for num,pokemon in enumerate(pokemon_list): 
            if choice == pokemon.get_name():
                pokemon_choice = deepcopy(pokemon_list[num])
                return pokemon_choice
            else: 
                continue 
        return None # no string matching user input was found 
    else: 
        index = int(choice) - 1
        try:
            pokemon_choice = deepcopy(pokemon_list[index])
            return pokemon_choice 
        except IndexError: # couldn't find pokemon based on choice input 
            return None 

def add_moves(pokemon, moves_list):
    ''''Adds four moves to a pokemon that theyll be able to use in battles'''
    pokemon_element1 = pokemon.get_element1()
    pokemon_element2 = pokemon.get_element2()
    
    length_of_list = len(moves_list)
    random_num = randint(0,length_of_list-1)
    random_move = moves_list[random_num]
    pokemon.add_move(random_move)
     
    for moves in range(200): # only check the first 200 moves, done out of simplicity 
        ran_num = randint(0,length_of_list-1)
        pok_move = moves_list[ran_num]
        if pok_move.get_element() == pokemon_element1 or pok_move.get_element() == pokemon_element2:
            
            if pok_move not in pokemon.get_moves(): # same move doesn't get added twice 
                pokemon.add_move(pok_move)
                
                if len(pokemon.get_moves()) == 4: 
                    return True 
        
    return False 

def turn(player_num, player_pokemon, opponent_pokemon):
    '''Will attack the opponent of the attacker, will determine if there is a winner \
        loer or if the game continues (due to sufficient hp of both parties)'''
    print("Player {}'s turn".format(player_num ))
    print(player_pokemon)
    while True:
        print("Show options: 'show ele', 'show pow', 'show acc'")
        show_option = input("Select an attack between 1 and 4 or show option or 'q': ").lower()
        if show_option == "q":
            if player_num == 1: 
                winner = 2
            else: 
                winner = 1
            print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, winner))
            return False 
        
        elif show_option == "show ele":
            player_pokemon.show_move_elements()
            continue
        
        elif show_option == "show pow":
            player_pokemon.show_move_power()
            continue 
            
        elif show_option == "show acc":
            player_pokemon.show_move_accuracy()
            continue 
        
        elif "1" <= show_option <= "4":
            index = int(show_option) - 1
            moves_list = player_pokemon.get_moves()
            move = moves_list[index]
            print("selected move: {}".format(move))
            print()
            
            opponent_s_hp = opponent_pokemon.get_hp()
            print("{} hp before:{}".format(opponent_pokemon.get_name(), opponent_s_hp))
            player_pokemon.attack(move, opponent_pokemon)
            opponent_new_hp = opponent_pokemon.get_hp()
            print("{} hp after:{}".format(opponent_pokemon.get_name(), opponent_new_hp))
            print()
            
            if opponent_new_hp == 0: 
                winner = player_num
                if winner == 1: 
                    loser = 2
                else: 
                    loser = 1 
                print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(loser, winner))
                return False
            else:
                return True 
            
        else: 
            show_option = input("Invalid option! Please enter a valid choice: ")
            continue 
         
            
def main():
    '''Runs the Pokemon game between two players'''
    
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()
        
    if usr_inp != 'y':
        print("Well that's a shame, goodbye")
        return
    
    else:
        fp1 = open("moves.csv", "r")
        moves_list = read_file_moves(fp1)
        fp1.close()
        
        fp2 = open("pokemon.csv", "r")
        pokemon_list = read_file_pokemon(fp2)
        fp2.close()
        
        p1_pokemon_choice = input("Player 1, choose a pokemon by name or index: ")
        p1_pokemon = choose_pokemon(p1_pokemon_choice, pokemon_list) # need to account for wrong input
        while True: 
            if p1_pokemon is None: # could not find the pokemon of their chooding 
                p1_pokemon_choice = input("Invalid option, choose a pokemon by name or index: ")
                p1_pokemon = choose_pokemon(p1_pokemon_choice, pokemon_list)
                continue 
            else: 
                print("pokemon{}:".format(1))
                print(p1_pokemon)
            
            
            while True: 
                add_move_1pok = add_moves(p1_pokemon, moves_list)
                if add_move_1pok == True: 
                    break
                
                else: 
                    print("Insufficient moves; choose a different pokemon.")
                    p1_pokemon_choice = input("Player 1, choose a pokemon by name or index: ") 
                    p1_pokemon = choose_pokemon(p1_pokemon_choice, pokemon_list)
                    continue 
            
            p2_pokemon_choice = input("Player 2, choose a pokemon by name or index: ")
            p2_pokemon = choose_pokemon(p2_pokemon_choice, pokemon_list)
            while True:
                if p2_pokemon is None: 
                    p2_pokemon_choice = input("Invalid option, choose a pokemon by name or index: ")
                    p2_pokemon = choose_pokemon(p2_pokemon_choice, pokemon_list)
                    continue 
                else: 
                    break 
            
            print("pokemon{}:".format(2))
            print(p2_pokemon)
            
            while True: 
                add_move_2pok = add_moves(p2_pokemon, moves_list)
                if add_move_2pok == True: 
                    break
                else: 
                    print("Insufficient moves; choose a different pokemon.") 
                    p1_pokemon_choice = input("Player 1, choose a pokemon by name or index: ") 
                    p1_pokemon = choose_pokemon(p1_pokemon_choice, pokemon_list)
                    continue 
        
             
            player_turn = 1 
            count = 0 
            while True: 
                if player_turn == 1: 
                    attacker = p1_pokemon 
                    opponent = p2_pokemon 
                else: 
                    attacker = p2_pokemon 
                    opponent = p1_pokemon 
                        
                game_answer = turn(player_turn, attacker, opponent)
                count += 1 
                if player_turn == 1: # alternat the turns
                        player_turn = 2
                else: 
                    player_turn = 1
                    
                if game_answer == True and count >= 2 and count % 2 == 0: # every two rounds if the players are still alive
                    print("Player {} hp after: {}".format(1, p1_pokemon.get_hp()))
                    print("Player {} hp after: {}".format(2, p2_pokemon.get_hp()))
                        
                    continue
                elif game_answer == True: 
                    continue 
                
                else:
                    cont_answer = input("Battle over, would you like to have another? ").lower()
                    while True: 
                        if cont_answer == "y": 
                            break 
                        elif cont_answer == "q" or cont_answer == "n":
                            print("Well that's a shame, goodbye")
                            break
                            pass
                        else: 
                            cont_answer = input("Invalid option! Please enter a valid choice: ")
                            continue 
                      
                    if cont_answer == "y": # gets you to the outter-most while loop
                        break
                    elif cont_answer == "q" or cont_answer == "n": 
                        break
                        
            if cont_answer == "y":
                p1_pokemon_choice = input("Player 1, choose a pokemon by name or index: ")
                p1_pokemon = choose_pokemon(p1_pokemon_choice, pokemon_list) 
                continue
            
            elif cont_answer == "q" or cont_answer == "n": # breaks out of the game 
                break
    
if __name__ == "__main__":
    main()

