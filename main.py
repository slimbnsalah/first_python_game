from tkinter import *
import random

MAX_CASES=63


def initialize_game():
    global game_board, players, permission_to_play, blocked_rounds, nbr_players, game_round, dice_case_enabled

    game_board=[]            #main game board where game happens
    for i in range (0,100):  #max cases for players to play in (needs to be at least max_cases + 12)
        game_board.append(0) #0 if nobody is in that case, else shows Player{i}
    players=[""]             #initialized to avoid using index 0, saves each player
    game_board[0]=players    #case depart 0, where all players start
    permission_to_play=[""]  #initialized to avoid using index 0, saves status of each player, if he's allowed to play or not
    blocked_rounds=[""]      #initialized to avoid using index 0, saves status of each player, how many rounds is he not allowed to play

    nbr_players= int (input("Enter Number of Players: "))
    """ nbr_players=3 """

    for i in range (1,nbr_players+1):
        players.append(f'Player{i}')
        permission_to_play.append(True)
        blocked_rounds.append(0)
        
    game_round=0
    dice_case_enabled=True


def generate_dice():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    list_dice=[dice1,dice2,dice1+dice2]
    print(f"DICES: {list_dice}\n")
    return list_dice


def check_if_destination_got_player_blocked(new_pos): #to free the past player there if applicable
    if new_pos in [19,31]:      #hotel or puit
        if game_board[19]!=0:
            j=int (game_board[19][-1])     #gets index of player in that case (last char)
            permission_to_play[j]=True
            blocked_rounds[j]=0
        elif game_board[31]!=0:
            j=int(game_board[31][-1])
            permission_to_play[j]=True
            blocked_rounds[j]=0
    elif new_pos ==52:      #prison
        if game_board[52]!=0:
            j= int(game_board[52][-1])
            blocked_rounds[j]=0


def check_double_dice(dice1,dice2):
    double_dice=False
    if (dice1==dice2):
        double_dice=True
    return double_dice


def move_player_with_step(i,step):
    
    if (f'Player{i}') in game_board[0]:
        old_pos=game_board[0].index(f'Player{i}')
        new_pos=step
        print("ACTION: STARTING FIRST MOVE -- Player%d moves from 0 to %d with Step= %d\n"%(i,new_pos,step))
        if game_board[new_pos]!=0:
            print(f"ACTION: SWITCHING PLAYERS POSITIONS -- Player{i} & {game_board[new_pos]} between 0 & {new_pos}")
        game_board[0][old_pos] , game_board[new_pos] = game_board[new_pos]  , game_board[0][old_pos] #switch list contents
        
    else: #player not in case depart 0
        old_pos=game_board.index(f'Player{i}')
        new_pos=old_pos+step
        print("ACTION: MOVING WITH STEP -- Player%d moves from %d to %d with Step= %d\n"%(i,old_pos,new_pos,step))
        if game_board[new_pos]!=0:
            print(f"ACTION: SWITCHING PLAYERS POSITIONS -- Player{i} & {game_board[new_pos]} between {old_pos} & {new_pos}")
        game_board[old_pos] , game_board[new_pos] = game_board[new_pos] , game_board[old_pos]   #switch list contents
    return new_pos


def move_player_to(i,destination):

    if (f'Player{i}') in game_board[0]:
        old_pos=game_board[0].index(f'Player{i}')
        if game_board[destination]!=0:
            print(f"ACTION: SWITCHING PLAYERS POSITIONS -- Player{i} & {game_board[destination]}")
        game_board[0][old_pos],game_board[destination]=game_board[destination],game_board[0][old_pos]
        old_pos=0 #only for display

    else:
        old_pos=game_board.index(f'Player{i}')
        if game_board[destination]!=0:
            print(f"ACTION: SWITCHING PLAYERS POSITIONS -- Player{i} & {game_board[destination]}")
        game_board[old_pos],game_board[destination]=game_board[destination],game_board[old_pos]
    print("ACTION: MOVING TO DESTINATION -- Player%d moves from %d to %d\n"%(i,old_pos,destination))


def check_dice_case(i,dice1,dice2):
    if (dice1==3 and dice2==6) or (dice1==6 and dice2==3):
        print("DICE CASE ACTIVATED -- You will move to Case 26")
        move_player_to(i,26)
        dice_case_done=True
    elif (dice1==4 and dice2==5) or (dice1==5 and dice2==4):
        print("DICE CASE ACTIVATED -- You will move to Case 53")
        move_player_to(i,53)
        dice_case_done=True
    else:
        dice_case_done=False
    return dice_case_done
 

def check_for_special_case(i,player_position):
    while player_position in [18,27,36,45,54]: #oie
        player_position=move_player_with_step(i, step)
        print("Oie")
     
    if player_position==6: #pont
        move_player_to(i,12)
        print("Pont")

    elif player_position==19: #hotel
        permission_to_play[i]=False
        blocked_rounds[i]=3
        print("Hotel")

    elif player_position==31: #puit
        permission_to_play[i]=False
        blocked_rounds[i]=999
        print("Puit")

    elif player_position==42: #lab
        move_player_to(i,30)
        print("Laby")

    elif player_position==52: #prison
        blocked_rounds[i]=999
        print("Prison")

    elif player_position==58: #mort
        global dice_case_enabled
        game_board[58]=0
        players.append(f"Player{i}")
        dice_case_enabled=True
        print("Mort")


def check_if_passed_final_case(i,player_position):
    if player_position>MAX_CASES:
        print("PASSED LAST CASE ---- RECALLING\n")
        move_player_to(i,MAX_CASES-(player_position-MAX_CASES)) #recall with remaining steps



##MAIN FONCTION::

initialize_game()

while game_board[MAX_CASES]==0:     #MAIN GAME LOOP 
    
    game_round+=1
    
    for i in range (1,nbr_players+1):   #Entring Player i Round
        print(f"\n        ########## Player {i} Playing in ROUND {game_round} ##########")
        
        try:
            old_pos=game_board.index(f'Player{i}')
            #TEST   Print("Test 3")
        except:
            old_pos=0
            #TEST   Print("Test 4")

        print(f"\nCurrent Position for Player{i}: {old_pos}")

        if permission_to_play[i]==True: #and blocked_rounds[i]<=0:
            #   Manual dice entry for test
            """ dice1=int (input("dice1: "))
            dice2=int (input("dice2: "))
            step=dice1+dice2 """
            #   Automatic dice generation
            input("\nPress Enter to Play ")
            dice_list=generate_dice()
            dice1=dice_list[0]
            dice2=dice_list[1]
            step=dice_list[2]
            
            new_pos=old_pos+step
            check_if_destination_got_player_blocked(new_pos)    #free other players from restrictions before making new move and switching with new player

            if blocked_rounds[i]>0:     #player in prison
                double_dice=check_double_dice(dice1, dice2)
                if double_dice==True:
                    print("GOT DOUBLE, OUT OF PRISON !")
                    blocked_rounds[i]=0
                    #   Manual dice entry for test
                    """ dice1=int (input("dice1: "))
                    dice2=int (input("dice2: "))
                    step=dice1+dice2 """
                    #   Automatic dice generation
                    input("\nPress Enter to Play ")
                    dice_list=generate_dice()
                    step=dice_list[2]
                    move_player_with_step(i, step)
                    
            if dice_case_enabled==True:     #if dice case is activated, only in first round or when player steps in Case 58 "Mort"
                dice_case_done=check_dice_case(i,dice1,dice2)   #True if player got 9 (6+3 or 4+5) and mouvement is done, therefore no need to continue the loop
                #TEST   print("Test 1",dice_case_enabled,dice_case_done)              
                
            if dice_case_done==False and blocked_rounds[i]<=0: #Move player normally with generated step if dice case mouvement wasn't done
                move_player_with_step(i,step)        
                #TEST   print("Test 2",dice_case_enabled,dice_case_done)


            check_for_special_case(i,new_pos)

            check_if_passed_final_case(i, new_pos)
            
            for j in range (0,MAX_CASES+1): #Loop for display
                print("Case: %d :  %s" % (j,game_board[j]) )
                
            #TEST print(permission_to_play,blocked_rounds)


        else: #if player is not permitted to play
            print(f"Player{i} is not permitted to play for {blocked_rounds[i]} rounds")   


        blocked_rounds[i]-=1
        if blocked_rounds[i]<=0:
            permission_to_play[i]=True


        if new_pos==MAX_CASES: #first player to reach the end of game board wins therefore game stops
            break


    dice_case_enabled=False #dice case only available in first round or Player in Case 58 "Mort"
    dice_case_done=False

print("\n                 #####     Winner is: ",game_board[MAX_CASES],"    #####")
#END OF PROGRAM