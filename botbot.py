#!/bin/python
def calculate_bid(player,pos,first_moves,second_moves):

    remaining = remaining_amount(player, first_moves, second_moves)
    
    amortized_bid = remaining / steps_remaining(player, pos)
    
    if player == 1:
        if pos == 1:
            return remaining
        else:
            # If last opponent move was greater than $10, 
            # bet amount that will still allow 
            # $10 dollars for each remaining step
            return min(amortized_bid, 14)
            
    else:
        if pos == 9:
            return remaining
        else:
            return min(amortized_bid, 14)

def steps_remaining(player, pos):
    if player == 1:
        return pos
    else:
        return 10 - pos

def get_draw_advantage_holder(first_moves, second_moves):
    holder = 1
    draws = 0
    
    for i in range(0, len(first_moves)):
        if first_moves[i] == second_moves[i]:
            draws += 1
            
    if draws % 2 == 0:
        return 1
    else: 
        return 2
    
# def get_opponent(player):
#     if(player == 1):
#         return 2
#     else:
#         return 1
        
# def get_opponents_remaining_amount(player, first_moves, second_moves):
#     opponent = get_opponent(player)
    
#     return remaining_amount(opponent, first_moves, second_moves)
    
#Calculate how much we've spent
def remaining_amount(player, first_moves, second_moves):
    
    starting_amount = 100
    first_spent = 0
    second_spent = 0
    
    for i in range(0, len(first_moves)):
        if first_moves[i] > second_moves[i]:
            first_spent += first_moves[i]        
        elif first_moves[i] < second_moves[i]:
            second_spent += second_moves[i]    
        else:
            trimmed_first = first_moves[:i]
            trimmed_second = second_moves[:i]
            
            # get current draw advantage
            holder = get_draw_advantage_holder(trimmed_first, trimmed_second)
            
            if(holder != 1):
                second_spent += second_moves[i]
            else:
                first_spent += first_moves[i]
        
    if player == 1:
        return starting_amount - first_spent
    else:
        return starting_amount - second_spent
    
#gets the id of the player
player = input()

scotch_pos = input()         #current position of the scotch

first_moves = [int(i) for i in raw_input().split()]
second_moves = [int(i) for i in raw_input().split()]
bid = calculate_bid(player,scotch_pos,first_moves,second_moves)
print bid
