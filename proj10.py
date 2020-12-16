################################################################################
#   Computer Project #10
#       
#   Algorithm 
#   The program allows the user to play Scorpion Solitaire. When the game starts
#   it will display a welcome message, the stock, the foundation, and the tableau
#   They will also be shown a list of options that will allow the to play the 
#   game accordingly. Based on what they chose the appropriate suite will run. 
#   So long as the user doesn't enter "q" or "Q" the program will continue to 
#   the game will continue to run, this includes if the user wins, at that point
#   another game will start automatically. Once the user desides to quit a thank
#   you message will be printed.
################################################################################

import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)

MENU = '''     
Input options:
    D: Deal to the Tableau (one card to first three columns).
    M c r d: Move card from Tableau (column,row) to end of column d.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def initialize():
    '''Initialize the stock, the foundation, and the tableau'''
    stock = cards.Deck()
    stock.shuffle()
    foundation = [[],[],[],[]] 
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    tableau = [list1, list2, list3, list4, list5, list6, list7]
    for count in range(7):
        if count < 3: # accounts for the 9 cards that need to be flipped down          
            card1 = stock.deal()
            card1.flip_card()
            list1.append(card1)
            
            card2 = stock.deal()
            card2.flip_card()
            list2.append(card2)
            
            card3 = stock.deal()
            card3.flip_card()
            list3.append(card3)
        else:
            list1.append(stock.deal())
            list2.append(stock.deal())
            list3.append(stock.deal())
        list4.append(stock.deal())
        list5.append(stock.deal())
        list6.append(stock.deal())
        list7.append(stock.deal())
    
    return (stock, tableau, foundation)            
    

def display(stock, tableau, foundation):
    '''Display the stock and foundation at the top.
       Display the tableau below.'''
       
    print("\n{:<8s}{:s}".format( "stock", "foundation"))
    if stock.is_empty():
        print("{}{}".format( " ", " "),end='') # fill space where stock would be so foundation gets printed in the right place
    else:
        print("{}{}".format( " X", "X"),end='')  # print as if face-down
    for f in foundation:
        if f:
            print(f[0],end=' ')  # print first card in stack(list) on foundation
        else:
            print("{}{}".format( " ", " "),end='') # fill space where card would be so foundation gets printed in the right place
            
    print()
    print("\ntableau")
    print("   ",end=' ')
    for i in range(1,8):
        print("{:>2d} ".format(i),end=' ')
    print()
    # determine the number of rows in the longest column        
    max_col = max([len(i) for i in tableau])
    for row in range(max_col):
        print("{:>2d}".format(row+1),end=' ')
        for col in range(7):
            # check that a card exists before trying to print it
            if row < len(tableau[col]):
                print(tableau[col][row],end=' ')
            else:
                print("   ",end=' ')
        print()  # carriage return at the end of each row
    print()  # carriage return after printing the whole tableau
    
def deal_from_stock(stock, tableau): 
    '''Will deal the last bit of cards left in the stock'''
    if len(stock) > 0: # only three cards will be left in the stock after the game starts 
        tableau[0].append(stock.deal())
        tableau[1].append(stock.deal())
        tableau[2].append(stock.deal())
    else: 
        pass
def validate_move(tableau, src_col, src_row, dst_col): 
    '''Decides if a move that was requested is legally allowed'''
    try: 
        current_list_2_check = src_col # the one off index is taken care off in the main function    
        current_ele_2_check = src_row  
        current_card = tableau[current_list_2_check][current_ele_2_check]
        current_card_suit = current_card.suit() 
        current_card_rank = current_card.rank()
        
        next_list_2_check = dst_col 
        try:
            next_card = tableau[next_list_2_check][-1]
            next_card_suit = next_card.suit() 
            next_card_rank = next_card.rank()
        except IndexError: 
            next_card = None
            next_card_suit = None 
            next_card_rank = None
    
    except IndexError: # if the user puts in a number that is too high
        return False 
    
    if (current_card_suit == next_card_suit) and ((current_card_rank + 1) == next_card_rank): # suits and rank match
        return True 
    elif current_card_rank == 13 and next_card == None: # if a row is empty and the user is moving a King
        return True
    else: 
        return False 
    
def move(tableau, src_col, src_row, dst_col):
    '''If the move was validated, then the appropriate cards will be moved'''
    validation = validate_move(tableau, src_col, src_row, dst_col)
    if validation == True: 
        current_list_2_check = src_col 
        current_ele_2_check = src_row 
        cards_moved = []
        for card in tableau[current_list_2_check][current_ele_2_check:]: 
            index = tableau[current_list_2_check].index(card)
            current_card = tableau[current_list_2_check].pop(index)
            cards_moved.append(current_card)
        
        next_list_2_check = dst_col 
        tableau[next_list_2_check].extend(cards_moved)
        
        if tableau[current_list_2_check] == []: 
            return True 
        elif not tableau[current_list_2_check][-1].is_face_up(): # account for the 9 cards that were never turned up
            tableau[current_list_2_check][-1].flip_card()
            return True
        else: 
            return True
        
    else: 
        return False 
    
def check_sequence(column_lst): 
    '''Checks if a list starts with a King and ends with an Ace ultimately \
        determining if the list will be moved to the foundation'''
    temp_s_card_lst = []
    temp_r_card_lst = []
    
    if len(column_lst) == 13: # all 13 cards are theoretically there 
        
        if column_lst[0].rank() == 13: # the first card is a king 
            for card in column_lst: 
                if card.suit() == column_lst[0].suit():
                   temp_s_card_lst.append(card)
                   
                else: 
                   return False # not all the caards of the same suit 
              
            if len(temp_s_card_lst) == len(column_lst): # there are still 13 cards left to check
               last_card_checked = column_lst[0]
               for card in column_lst[1:]:
                   if card.rank() + 1 == last_card_checked.rank():
                       temp_r_card_lst.append(card)
                       last_card_checked = card
                   else: 
                       return False # not in decending order from 13
            else: 
                return False # if the number of cards aren't the same as when we started 
            return True # winning sequence 
        else: 
            return False # if the first card isn't king
    else: 
        return False # if the list isn't long enough 
def move_to_foundation(tableau, foundation): 
    '''Will shift through the tableau finding all list that qualify to be added \
        any list that qualifies will be added to the foundation'''
    fir_f, sec_f, thr_f, four_f = foundation[0], foundation[1], foundation[2], foundation[3] 
    
    for lst in tableau:
        answer = check_sequence(lst)  
        if answer == True:
            if fir_f == []: 
                for i in range(13): 
                    current_card = lst.pop(0) 
                    fir_f.append(current_card)
                    
            elif sec_f == []:
                for i in range(13): 
                    current_card = lst.pop(0) 
                    sec_f.append(current_card)
                    
            elif thr_f == []: 
                for i in range(13): 
                    current_card = lst.pop(0) 
                    thr_f.append(current_card) 
                    
            else: 
                for i in range(13): 
                    current_card = lst.pop(0) 
                    four_f.append(current_card)
                        
        else: 
            continue 
        
def check_for_win(foundation):
    '''Check if the foundation is filled'''
    fir_f, sec_f, thr_f, four_f = foundation[0], foundation[1], foundation[2], foundation[3]
    if len(fir_f) == 13: 
        if len(sec_f) == 13: 
            if len(thr_f) == 13: 
                if len(four_f) == 13: 
                    return True 
                else: 
                    return False
            else: 
                return False
        else: 
            return False
    else: 
        return False

def get_option():
    '''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    D: Deal to the Tableau (one card to first three columns).
    M c r d: Move card from Tableau column,row to end of column d.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
    '''
    option = input( "\nInput an option (DMRHQ): " )
    option_list = option.strip().split()
    
    opt_char = option_list[0].upper()
    
    if opt_char in 'DRHQ' and len(option_list) == 1:  # correct format
        return [opt_char]

    if opt_char == 'M' and len(option_list) == 4 and option_list[1].isdigit() \
        and option_list[2].isdigit() and option_list[3].isdigit():
        return ['M',int(option_list[1]),int(option_list[2]),int(option_list[3])]

    print("Error in option:", option)
    return None   # none of the above
 
def main():
    '''Run the main program in order to play the game'''
    print("\nWelcome to Scorpion Solitaire.\n")
    stock, tableau, foundation = initialize()
    display(stock, tableau, foundation)
    print(MENU)
    option_lst = get_option()
    
    while option_lst and option_lst[0] != 'Q':
        if option_lst[0] == "D":
            deal_from_stock(stock, tableau)
            display(stock, tableau, foundation)
        
        elif option_lst[0] == "M": 
            move_answer = move(tableau, option_lst[1] - 1, option_lst[2] -1, option_lst[3] - 1) # account for index
            if move_answer == True: 
                move_to_foundation(tableau, foundation)
                win_answer = check_for_win(foundation)
                if win_answer == True: 
                    print("You won!")
                    print()
                    print("New Game.")
                    stock, tableau, foundation = initialize()
                    display(stock, tableau, foundation)
                    print(MENU)
                    option_lst = get_option()
                    continue 
        
            else: 
                print("Error in move:",option_lst[0],",",option_lst[1],",",option_lst[2],",",option_lst[3])
                option_lst = get_option()
                continue
            display(stock, tableau, foundation)
        
        elif option_lst[0] == "R": 
            stock, tableau, foundation = initialize() # shuffles cards before a new game
            display(stock, tableau, foundation)
            print(MENU)
        
        elif option_lst[0] == "H":
            print(MENU)
        
        else: # move failed
            print("Error in move:",option_lst[0],",",option_lst[1],",",option_lst[2],",",option_lst[3])
        option_lst = get_option()
    
    print("Thank you for playing.")

if __name__ == '__main__':
    main()
