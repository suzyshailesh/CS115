#Susmitha Shailesh
#I pledge my honor that I have abided by the Stevens Honor System.

# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:
            print("Congrats! You won :)")

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:
            print("Sorry, you lost the game :(")

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    
    num_piles = int(input("How many piles do you want to play with?\n"))
    piles = [0]*num_piles

    for i in range(num_piles):
        piles[i] = int(input("How many in pile " + str(i) + "?\n"))


        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    for i in range(num_piles):
        print("pile " + str(i) + " = " + str(piles[i]))


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    user_input = int(input("Which pile?\n"))

    while(valid_pile_choice(user_input) == False):
        user_input = int(input("Try again. Which pile?\n"))

    return user_input

def valid_pile_choice(x):
    '''checks to see if user's pile choice is valid'''
    global num_piles
    global piles
    
    if x in range(0,num_piles):
        if piles[x] == 0:
            return False
        else: return True
    else: return False


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles

    user_input = int(input("How many?\n"))

    while(valid_number_choice(user_input, piles[pnum]) == False):
        user_input = int(input("Try again. How many?\n"))

    return user_input

def valid_number_choice(x, y):
    '''checks to see if user's number choice is valid'''
    if x in range(1,y+1):
        return True
    else: return False


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 

    nim_sum = 0

    for index in piles:
        nim_sum = nim_sum^index

    return nim_sum


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 

    pile_sums = [0] * len(piles)

    for index in range(len(piles)):
        pile_sums[index] = piles[index] ^ game_nim_sum()

    pile_choice = which_pile(piles, pile_sums)

    if pile_choice == -1:
        for i in range(len(piles)):
            if piles[i] > 0:
                pile_choice = i
                print(pile_choice)
                break
        how_many = 1
    else: how_many = piles[pile_choice] - pile_sums[pile_choice]

    return (pile_choice, how_many)


def which_pile(piles, sums):
    '''finds the pile with a pile_sum less than its number of coins'''
    for index in range(len(piles)):
        if sums[index] < piles[index]:
            return index
    return -1


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    print("Okay, it's my turn now.")

    comp_turn = opt_play()
    turn_pile = comp_turn[0]
    turn_coins = comp_turn[1]

    piles[turn_pile] = piles[turn_pile] - turn_coins

    print("I remove " + str(turn_coins) + " from pile " + str(turn_pile))

    
    


#   start playing automatically
if __name__ == "__main__" : play_nim()
