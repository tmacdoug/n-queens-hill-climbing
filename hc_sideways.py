import random
import copy

from utility import print_board, calculate_h, initialize_board


#Sideways move: always keep a record of previous states, and check that no states are repeated

#board: 2D array representing the chessboard
#h: current heuristic value
#steps: number of steps taken so far
#record_seq: array containing all previous board states (defaults to false if not asked to record)
def hill_climb_with_sideways_move(board, h, steps, record_seq, random_restart=False, restarts_tot=0):
    n = len(board)
    next_state = False

    #If recording the state sequence— add to record
    record_seq.append(board)

    #Search for each queen
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                #Queen found, generate all possible neighbors
                #Neighbors are generated as per the slides (moving the queen within its column)

                #Temporarily remove queen to avoid duplicates
                board[row][col] = 0
                for new_row in range(n):
                    if new_row != row and board[new_row][col] != 1: #Skip the current position of the queen
                        new_board = copy.deepcopy(board)
                        new_board[new_row][col] = 1
                        if new_board not in record_seq: #Ensure states are not repeated
                            #Calculate heuristic
                            new_h = calculate_h(new_board)
                            
                            #If new state's heuristic is better (or same— sideways move) than previous, consider that state for the next iteration
                            if new_h <= h: 
                                h = new_h
                                next_state = copy.deepcopy(new_board)
                #Replace the original queen, and continue onto the next
                board[row][col] = 1

    if next_state == False: #No neighbor had a better (or equal) heuristic, so the search has ended
        #Return stats
        ret = {
            'success': False,
            'steps': steps,
            'seq': record_seq
        }
        #If random restart, incremement restarts, initialize new random board, and begin search again
        if random_restart:
            restarts_tot += 1
            new_board = initialize_board(len(board))
            return hill_climb_with_sideways_move(new_board, calculate_h(new_board), steps, [], random_restart=random_restart, restarts_tot=restarts_tot)
        else: return ret
    elif h == 0: #We've reached a completed state
        #If recording the state sequence— add to record
        record_seq.append(next_state)

        #Return stats
        ret = {
            'success': True,
            'steps': steps,
            'seq': record_seq
        }
        #If random restarts: append total number of restarts to stats
        if random_restart: ret['restarts'] = restarts_tot
        return ret
    else:
        return hill_climb_with_sideways_move(next_state, h, steps+1, record_seq=record_seq, random_restart=random_restart, restarts_tot=restarts_tot)