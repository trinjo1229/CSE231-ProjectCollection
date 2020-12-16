###############################################################################
#   Computer Project #4 
#
#   Algorithm 
#       
#       while the answer is one of the options from the main menu run the 
#       appropriate suite
#       options available include 
#           * converting a decimal number into another base
#           * converting a decimal number from another base 
#           * converteting from one representation system to another
#           * displaying the sum of binary numbers 
#           * compressing a given image
#           * uncompressing a given image 
#           * display the menu of options
#           * exit the program 
#       once the appropriate suite runs ask for another option 
#       if this option is "x" or "X" then stop the while loop and print 
#       a goodbye message 
###############################################################################

def display_options():
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             D. Display the sum of two binary numbers.
             E. Compress an image.
             U. Uncompress an image.
             M. Display the menu of options.
             X. Exit from the program.'''
       
    print(MENU)
    return ""

def numtobase(N, B):
    '''converts a number into a desried base'''
    N = int(N)
    B = int(B)
    ori_quotient = N 
    base_num = "" 
    new_quotient = N
    remainder = 0
    stored_quotient = 0 
    if N == 0: 
        return ""
    while (ori_quotient > 0) and (new_quotient > 0): 
        stored_quotient = new_quotient // B
        remainder = new_quotient % B
        base_num += str(remainder)
        new_quotient = stored_quotient 
    else: 
        return str(base_num[::-1])
 
def basetonum(S, B):
    '''converts any other based number to base 10'''
    if S == "":
        return 0
    
    exponent = len(S) - 1  #compensates for the 0th index
    number = int(S)
    base = int(B)
    
    if 2 <= base <= 10:  
        b_10_num = 0
        
        if number == '':
            return 0
            
        while exponent >= 0: 
            number = str(S)
            for n,l in enumerate(S):
                l = int(l)
                place = (l * (base ** exponent))
                exponent -= 1
                b_10_num += place
        else: 
            answer = b_10_num
            return answer
    
def basetobase (B1,B2,S_1):
    '''changes a given base number into another wanted base'''
    conversion_num = basetonum(S_1,B1)
    final_number = numtobase(conversion_num,B2)
    return final_number

def addbinary(S, T):
    '''adds binary #'s together'''
    bi_num_1 = basetonum(S,2) # the 2 implies that I wan't my answer in binary
    bi_num_2 = basetonum(T,2)
    new_number = (bi_num_1 + bi_num_2)
    answer = numtobase(new_number, 2)
    return answer 

def compress(S):
    '''takes a binary string and returns its compressed binary string'''
    if S == "":
        return ""
    
    index_value = S[0]
    index_value_count = 0
    compressed_string = ""
    bit_string = ""
    
    for index, number in enumerate(S):
        while index_value == number:
            index_value_count += 1 
            break
        if index_value != number:
            binary_value = numtobase(index_value_count,2) # want the answer in base 2
            bit_string = binary_value.zfill(7) # fill to 7 to compensate for the index I have ignored
            bit_string = index_value + bit_string
            compressed_string += bit_string 
            index_value = number 
            index_value_count = 1 # the one compensates for the index you're currently at
            bit_string = ""
            
    if (index_value * index_value_count) == (number * index_value_count):
        binary_value = numtobase(index_value_count,2)
        binary_value = binary_value.zfill(7)
        bit_string = index_value + binary_value
        compressed_string += bit_string
    
    return(compressed_string)

def uncompress(S):
    '''uncompresses a string and gives you back its original binary form'''
    if S == "":
        return ""
    uncompressed_str = ""
    index_value = S[0]
    current_start_index = 0
    current_end_index = 8 # allows me to focus on the first 8 digits
    bit_count = 8
    length = len(S) 
    
    while bit_count <= length: 
        current_8 = S[current_start_index:current_end_index]
        binary_num_start = current_8.find("1",1,-1)
        binary_num_b2 = current_8[binary_num_start:current_end_index]
        binary_num_b10 = basetonum(binary_num_b2,2)
        uncompressed_str += (index_value * binary_num_b10)
        bit_count += 8 # checks the next 8 digits
        
        if (length > 8) and (bit_count <= length):
            index_value = S[current_end_index]
            current_start_index += 8  
            current_end_index += 8
            current_8 = ""
        else: 
            break
    return uncompressed_str

def main():
    
    BANNER = '''
        .    .        .      .             . .     .        .          .          .
         .                 .                    .                .
  .               A long time ago in a galaxy far, far away...   .
              .   A terrible civil war burns throughout the  .        .     .
                 galaxy: a rag-tag group of freedom fighters   .  .
     .       .  has risen from beneath the dark shadow of the            .
.        .     evil monster the Galactic Empire has become.                  .  .
    .      Outnumbered and outgunned,  the Rebellion burns across the   .    .
.      vast reaches of space and a thousand-thousand worlds, with only     .
    . their great courage - and the mystical power known as the Force -
     flaming a fire of hope. a                                   .

              .------.
            .'::::::' `.
            |: __   __ |
            | <__] [__>|
            `-.  __  .-'
              | |==| |
              | |==| |
           __.`-[..]-`\__
    _.--:``      ||   _``:::--._
   | |  |.      .:'  (o) ::|  | |
   |_|  |::..  // _       :|  |_|
    ===-|:``` // /.\       |-===
   |_| `:___//_|[ ]|_____.' |_| )
    l=l   |\V/_=======_==|   l=l/
  .-l=l   |`'==/=="======|  /|.:
  | l l   |=="======\=_==| `-T l
  `.l_l   |==============|   l_l
    [_]  [__][__]____[_]__]  [_]
    \\\ .'.--.- --   --. .`. |||.
    \\\\| |  |    |    |  || ||||
     \\\\   .'    |    |  |`.||||   
      \\\\  |  LS |    `.   |||||     


    
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~    
                
    '''
    print(BANNER)
    print('''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             D. Display the sum of two binary numbers.
             E. Compress an image.
             U. Uncompress an image.
             M. Display the menu of options.
             X. Exit from the program.''')
    
    answer = "a"
    question = input("\n\tEnter option: ")
    answer = question.lower()
        
    while (answer != "a") and (answer != "b") and (answer != "c") and (answer != "d") and (answer != "e") and (answer != "u") and (answer != "m"):
            print("\n\tError:  unrecognized option [{}]".format(answer.upper()))
            print('''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             D. Display the sum of two binary numbers.
             E. Compress an image.
             U. Uncompress an image.
             M. Display the menu of options.
             X. Exit from the program.''')
            question = input("\n\tEnter option: ")
            answer = question.lower()
            continue
        
    while (answer == "a") or (answer == "b") or (answer == "c") or (answer == "d") or (answer == "e") or (answer == "u") or (answer == "m"):
        
        while answer == "a":
            N = input("\n\tEnter N: ")
            
            while N.isdigit():
                B = input("\n\tEnter Base: ")
                B_int = int(B)
                break
            else: 
                print("\n\tError: {} was not a valid non-negative integer.".format(N))
                continue          
                
            while (B_int < 2) or (B_int > 10):
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B)) 
                B = input("\n\tEnter Base: ")
                B_int = int(B)
                
            if 2 <= B_int <= 10:
                B_int = str(B)
                answer = numtobase(N, B)
                print("\n\t {} in base {}: {}".format(N, B_int, answer))
                
        while answer == "b":
            S = input("\n\tEnter string number S: ")
            B = input("\n\tEnter Base: ")
            B = int(B)
            
            while (B < 2) or (B > 10):
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B)) 
                B = input("\n\tEnter Base: ")
                B = int(B)
                
            else: 
                answer = basetonum(S, B)
                print("\n\t {} in base {}: {}".format(S, B, answer))
                
        while answer == "c":
            B1 = input("\n\tEnter base B1: ")
            B1 = int(B1)
            
            while (B1 < 2) or (B1 > 10):
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B1)) 
                B1 = input("\n\tEnter base B1: ")
                B1 = int(B1)
            else: 
                B2 = input("\n\tEnter base B2: ")
                B2 = int(B2)
            
            while (B2 < 2) or (B2 > 10):
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B2)) 
                B2 = input("\n\tEnter base B2: ")
                B2 = int(B2)
            else: 
                S_1 = input("\n\tEnter string number S: ")
                if S_1 == None:
                    print("\n\t {} in base {} is {} in base {}...".format(S_1, B1, 0, B2))
                else:
                    answer = basetobase(B1,B2,S_1)
                    print("\n\t {} in base {} is {} in base {}...".format(S_1, B1, answer, B2))
                    
        while answer == "d":
            S = input("\n\tEnter the first string number: ")
            T = input("\n\tEnter the second string number: ")
            answer = addbinary(S, T)
            print("\n\tThe sum: {}".format(answer))
            
        while answer == "e":
            S = input("\n\tEnter a binary string of an image: ")
            answer = compress(S)
            print("\n\t Original image: {}".format(S))
            print("\n\t Run-length encoded image: {}".format(answer))
            
            
        while answer == "u":
            S = input("\n\tEnter a run-length encoded string of an image: ")
            answer = uncompress(S)
            print("\n\t Run-length encoded image: {}".format(S))
            print("\n\t Original image: {}".format(answer))
         
        while answer == "m":
            print(display_options())
            break
        
        question = input("\n\tEnter option: ")
        answer = question.lower()
        if answer == "x":
            print('May the force be with you.')
            break  
 
                
if __name__ == "__main__":
    main()


