import numpy as np
import time
import os

#Change the size of x and y.
maze = np.full((10,20),'#')
maze[0] = ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
maze[1] = ['#',' ',' ',' ','#',' ','#',' ',' ','#','#',' ',' ',' ','#',' ','#',' ','#','#']
maze[2] = ['#',' ','#',' ','#',' ','#',' ','#','#','#',' ','#',' ','#',' ','#',' ','#','#']
maze[3] = ['#',' ','#',' ',' ',' ',' ',' ',' ','#','#',' ','#',' ',' ',' ',' ',' ',' ','#']
maze[4] = ['#','#','#','#','#',' ','#','#',' ','#','#','#','#','#','#',' ','#','#',' ','#']
maze[5] = ['#',' ',' ',' ','#',' ',' ','#',' ','#','#',' ',' ',' ','#',' ',' ','#',' ','#']
maze[6] = ['#',' ','#',' ','#',' ','#',' ',' ',' ','#',' ','#',' ','#',' ','#',' ',' ','#']
maze[7] = ['#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#','#']
maze[8] = ['#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ']
maze[9] = ['#','#','#',' ','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']

def print_maze(arr):
    for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
            if arr[y][x] == '#':
                print('\033[96m' + arr[y][x] + '\033[0m', end ='')
            elif arr[y][x] == '*':
                print('\033[91m' + arr[y][x] + '\033[0m', end ='')
            else:
                print(arr[y][x], end ='')
        print()


def explore(maze, current_y, current_x, depth, solution):

	# update the current position in the solution
	solution.append((current_y, current_x))

	# Check if the current position is the exit
	if (current_y == 8 and current_x == 19):
		print_maze(maze)
		print("Found the exit! The solution path is:")
		for i, (y, x) in enumerate(solution):
			maze[y][x] = 'X'
			print_maze(maze)
			print("Step {}".format(i + 1))
			time.sleep(0.5)
		exit()

	maze[current_y][current_x] = '*'
	print_maze(maze)
	print("Current depth: {}".format(depth))
	time.sleep(0.5)
	os.system("cls||clear")

	# Check if it's possible to move up
	if current_y - 1 >= 0 and maze[current_y - 1][current_x] == ' ' :
		explore(maze.copy(), current_y - 1, current_x, depth + 1, solution.copy())

	# Check if it's possible to move down
	if current_y + 1 <= 9 and maze[current_y + 1][current_x] == ' ' :
		explore(maze.copy(), current_y + 1, current_x, depth + 1, solution.copy())
            
	# Check if it's possible to move left
	if current_x - 1 >= 0 and  maze[current_y][current_x - 1] == ' ' :
		explore(maze.copy(), current_y, current_x - 1, depth + 1, solution.copy()) 
        
	# Check if it's possible to move right
	if current_x + 1 <= 19 and maze[current_y][current_x + 1] == ' ':
		explore(maze.copy(), current_y, current_x + 1, depth + 1, solution.copy())

os.system("cls||clear")
explore(maze, 9, 3, 0, []) #Character starts at coordinate 3,9

