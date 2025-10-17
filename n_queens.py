#N-Queens Problem
#Thomas MacDougall
#ITCS 6150 Project 2

import random
import copy

from hill_climbing import vanilla_hill_climb 
from hc_sideways import hill_climb_with_sideways_move
from utility import print_board, calculate_h, initialize_board


if __name__ == "__main__":
    #Gather user input
    n = int(input("n = "))
    runs = int(input("How many times should each search be run? "))

    print('\nPart A: Vanilla Hill Climb')
    succ = 0
    succ_steps = 0
    fail_steps = 0
    for i in range(runs-4):
        #Create nxn board and initialize randomly
        board = initialize_board(n)

        res = vanilla_hill_climb(board, calculate_h(board), 0, record_seq=[])
        if res['success'] == True:
            succ += 1
            succ_steps += res['steps']
        else:
            fail_steps += res['steps']
    #Search sequences from four random initial configurations
    for i in range(runs - (runs-4)):
        #Create nxn board and initialize randomly
        board = initialize_board(n)

        res = vanilla_hill_climb(board, calculate_h(board), 0, record_seq=[])
        if res['success'] == True:
            succ += 1
            succ_steps += res['steps']
        else:
            fail_steps += res['steps']
        
        #Print search sequence
        print(f'Search sequence #{i+1}:')
        j = 0
        for board in res['seq']:
            print_board(board)
            if j != len(res['seq'])-1: print('   |\n   v\n')
            j+=1
    
    print(f'Successes: {succ} (Avg. steps taken: {succ_steps / succ})\t||\tFailures: {runs-succ} (Avg. steps taken: {fail_steps / (runs-succ)})\t||\tSuccess rate: {round(100*succ/runs, 1)}')

    print('\nPart B: Hill-Climbing Search with Sideways Move')
    succ = 0
    succ_steps = 0
    fail_steps = 0
    for i in range(runs-4):
        #Create nxn board and initialize randomly
        board = initialize_board(n)

        res = hill_climb_with_sideways_move(board, calculate_h(board), 0, [], random_restart=False)
        if res['success'] == True:
            succ += 1
            succ_steps += res['steps']
        else:
            fail_steps += res['steps']
    #Search sequences from four random initial configurations
    for i in range(runs - (runs-4)):
        #Create nxn board and initialize randomly
        board = initialize_board(n)

        res = hill_climb_with_sideways_move(board, calculate_h(board), 0, [])
        if res['success'] == True:
            succ += 1
            succ_steps += res['steps']
        else:
            fail_steps += res['steps']

        #Print search sequence
        print(f'Search sequence #{i+1}:')
        j = 0
        for board in res['seq']:
            print_board(board)
            if j != len(res['seq'])-1: print('   |\n   v\n')
            j+=1
    print(f'Successes: {succ} (Avg. steps taken: {succ_steps / succ})\t||\tFailures: {runs-succ} (Avg. steps taken: {fail_steps / (runs-succ)})\t||\tSuccess rate: {round(100*succ/runs, 1)}')
    

    print('\nPart C: Random-Restart Hill-Climbing Search')
    no_sideways_steps = 0
    sideways_steps = 0
    no_sideways_restarts = 0
    sideways_restarts = 0
    for i in range(runs):
        #Create nxn board and initialize randomly
        board = initialize_board(n)

        #Run without sideways moves
        res = vanilla_hill_climb(board, calculate_h(board), 0, [], random_restart=True, restarts_tot=0)

        no_sideways_restarts+=res['restarts']
        no_sideways_steps += res['steps']
        
        #Re-run with sideways moves
        res = hill_climb_with_sideways_move(board, calculate_h(board), 0, [], random_restart=True, restarts_tot=0)

        sideways_restarts+=res['restarts']
        sideways_steps += res['steps']

    print(f'Without Sideways Move:\n\tAvg. Restarts: {round(no_sideways_restarts/runs,1)}\n\tAvg. Steps:{round(no_sideways_steps/runs,1)}\
          \nWith Sideways Move:\n\tAvg. Restarts: {round(sideways_restarts/runs,1)}\n\tAvg. Steps:{round(sideways_steps/runs,1)}')