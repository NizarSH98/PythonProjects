from collections import deque
import random
import tkinter as tk
import time

root = tk.Tk()
root.title("9 Puzzle Game")

goalState = [
    1,2,3,
    4,5,6,
    7,8,0]

currentState = [
    1,2,3,
    4,5,0,
    7,8,6]

#list(range(9))  # Create a list from 0 to 8
#random.shuffle(currentState)  # Shuffle the list in place

def getSuccessors(currentState):
    zeroIndex = currentState.index(0)
    validMoves = []

    if zeroIndex % 3 > 0:  # Check if zero can move left
        validMoves.append("l")

    if zeroIndex % 3 < 2:  # Check if zero can move right
        validMoves.append("r")

    if zeroIndex >= 0 and zeroIndex <= 5:
        validMoves.append("d")

    if zeroIndex >= 3 and zeroIndex <= 8:
        validMoves.append("u")

    return validMoves

def update_labels(state):
    for i in range(3):
        for j in range(3):
            label = tk.Label(root, text=str(state[i*3 + j]), font=('Helvetica', 20), width=5, height=2, relief='ridge')
            label.grid(row=i, column=j)

update_labels(currentState)

def isGoalState(currentState,goalState):
    return (currentState==goalState)

def bfs(currentState, goalState):
    frontier = deque([(currentState, [])])  # Initialize the frontier queue with the initial state and an empty path
    explored = set()  # Initialize the set of explored states

    while frontier:
        

        state, path = frontier.popleft()  # Get the first state and its path from the queue

        if isGoalState(state, goalState):
            return path  # If the goal state is reached, return the path

        explored.add(tuple(state))  # Add the state to the set of explored states

        

        for move in getSuccessors(state):
            nextState = getNewState(state, move)
            if tuple(nextState) not in explored:
                frontier.append((nextState, path + [move])) # Add the next state and its path to the frontier
                update_labels(nextState)
                break
        
    return None  # If no solution is found, return None 


def getNewState(currentState, move):
    zeroIndex = currentState.index(0)
    newZeroIndex = zeroIndex

    if move == "l":
        newZeroIndex -= 1
    elif move == "r":
        newZeroIndex += 1
    elif move == "u":
        newZeroIndex -= 3
    elif move == "d":
        newZeroIndex += 3

    newState = list(currentState)
    newState[zeroIndex], newState[newZeroIndex] = newState[newZeroIndex], newState[zeroIndex]

    return newState

print(currentState[0],currentState[1],currentState[2])
print(currentState[3],currentState[4],currentState[5])
print(currentState[6],currentState[7],currentState[8])
print(bfs(currentState , goalState ))
result = bfs(currentState, goalState)

# Start the GUI event loop
#root.mainloop()

'''if result is not None:
    print("Solution found!")
    print(result)
else:
    print("No solution found.")'''