import numpy as np
from copy import deepcopy
import random

def init():
    global cube
    global opp_sides
    cube = {"top": [["G","B","Y"],
                    ["Y","W","B"],
                    ["G","R","Y"]],

            "left": [["Y","G","Y"],
                    ["Y","G","W"],
                    ["G","Y","G"]],

            "front": [["R","G","O"],
                    ["G","R","R"],
                    ["O","O","R"]],

            "right": [["B","R","B"],
                    ["W","B","W"],
                    ["W","O","W"]],

            "back": [["R","W","O"],
                    ["O","O","R"],
                    ["O","Y","R"]],

            "bottom": [["W","B","B"],
                    ["B","Y","G"],
                    ["W","O","B"]]
            }
    
    opp_sides = {"Y":"W", "W":"Y",
                "B":"G", "G":"B",
                "R":"O", "O":"R"}
    
def redundant_steps_remover(g_movements):
    g_movements_str = ' '.join(g_movements)
    while True:
        g_movements_init = g_movements_str
        g_movements_str = g_movements_str.replace("LEFT "*4, "")
        g_movements_str = g_movements_str.replace("LEFT "*3, "RIGHT ")
        g_movements_str = g_movements_str.replace("UP DN ", "")
        g_movements_str = g_movements_str.replace("LEFT RIGHT ", "")
        g_movements_str = g_movements_str.replace("RIGHT LEFT ", "")
        g_movements_str = g_movements_str.replace("RIGHT DN LEFT ", "ANTICLOCK ")
        g_movements_str = g_movements_str.replace("CLOCK "*3, "ANTICLOCK ")
        g_movements_str = g_movements_str.replace("LEFT BR "*4, "")
        g_movements_str = g_movements_str.replace("LEFT BR "*3, "RIGHT BL ")
        g_movements_str = g_movements_str.replace("TR "*4, "")
        g_movements_str = g_movements_str.replace("TR "*3, "TL ")
        g_movements_str = g_movements_str.replace("FR "*3, "FL ")
        g_movements_str = g_movements_str.replace("DN "*3, "UP ")
        g_movements_str = g_movements_str.replace("TR LEFT "*4, "")
        g_movements_str = g_movements_str.replace("TR LEFT "*3, "TL RIGHT ")
        g_movements_str = g_movements_str.replace("FR ANTICLOCK "*3, "FL CLOCK ")
#         g_movements_str = g_movements_str.replace("UP CLOCK DN ", "LEFT ")
        g_movements_str = g_movements_str.replace("LD "*3, "LU ")
        g_movements_str = g_movements_str.replace("BR LEFT BL ", "LEFT ")
        g_movements_str = g_movements_str.replace("ANTICLOCK CLOCK ", "")
        g_movements_str = g_movements_str.replace(" CLOCK FR ANTICLOCK ", " FR ")
        g_movements_str = g_movements_str.replace("RIGHT ANTICLOCK DN ", "ANTICLOCK ")

        if(g_movements_init == g_movements_str):
            break

    g_movements = g_movements_str.split()
    return g_movements

def shuffle():
    movements = ["FL", "FR", "DN", "UP", "LEFT", "RIGHT", "TL", "TR", "RU", "RD", "LU", "LD", "BL", "BR", "CLOCK", "ANTICLOCK"]
    n_moves = np.random.randint(20,300)
    for i in range(n_moves):
        move = random.choice(movements)
        update_cube(move)

def rotate90AntiClockwise(mat): 
    N = len(mat[0])
    # Consider all squares one by one 
    for x in range(0, int(N / 2)):  
        # Consider elements in group    
        # of 4 in current square 
        for y in range(x, N-x-1):  
            # store current cell in temp variable 
            temp = mat[x][y] 
            # move values from right to top 
            mat[x][y] = mat[y][N-1-x] 
            # move values from bottom to right 
            mat[y][N-1-x] = mat[N-1-x][N-1-y] 
            # move values from left to bottom 
            mat[N-1-x][N-1-y] = mat[N-1-y][x] 
            # assign temp to left 
            mat[N-1-y][x] = temp 

def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

def move_front_left():
    top = cube["top"][2].copy()
    rotate90AntiClockwise(cube["front"])

    for i in range(3):
        cube["top"][2][i] = cube["right"][i][0]
    for i in range(3):
        cube["right"][i][0] = cube["bottom"][0][2-i]
    for i in range(3):
        cube["bottom"][0][i] = cube["left"][i][2]
    for i in range(3):
        cube["left"][i][2] = top[2-i]

def move_front_right():
    top = cube["top"][2].copy()
    rotate90Clockwise(cube["front"])
    for i in range(3):
        cube["top"][2][i] = cube["left"][2-i][2]
    for i in range(3):
        cube["left"][i][2] = cube["bottom"][0][i]
    for i in range(3):
        cube["bottom"][0][i] = cube["right"][2-i][0]
    for i in range(3):
        cube["right"][i][0] = top[i]

def move_down():
    rotate90Clockwise(cube["left"])
    rotate90AntiClockwise(cube["right"])
    bottom = deepcopy(cube["bottom"])
    for i in range(3):
        for j in range(3):
            cube["bottom"][i][j] = cube["front"][i][j]
    for i in range(3):
        for j in range(3):
            cube["front"][i][j] = cube["top"][i][j]
    for i in range(3):
        for j in range(3):
            cube["top"][i][j] = cube["back"][2-i][2-j]
    for i in range(3):
        for j in range(3):
            cube["back"][i][j] = bottom[2-i][2-j]

def move_up():
    rotate90Clockwise(cube["right"])
    rotate90AntiClockwise(cube["left"])
    top = deepcopy(cube["top"])
    for i in range(3):
        for j in range(3):
            cube["top"][i][j] = cube["front"][i][j]
    for i in range(3):
        for j in range(3):
            cube["front"][i][j] = cube["bottom"][i][j]
    for i in range(3):
        for j in range(3):
            cube["bottom"][i][j] = cube["back"][2-i][2-j]
    for i in range(3):
        for j in range(3):
            cube["back"][i][j] = top[2-i][2-j]

def move_left():
    rotate90Clockwise(cube["top"])
    rotate90AntiClockwise(cube["bottom"])
    front = deepcopy(cube["front"])
    for i in range(3):
        for j in range(3):
            cube["front"][i][j] = cube["right"][i][j]
    for i in range(3):
        for j in range(3):
            cube["right"][i][j] = cube["back"][i][j]
    for i in range(3):
        for j in range(3):
            cube["back"][i][j] = cube["left"][i][j]
    for i in range(3):
        for j in range(3):
            cube["left"][i][j] = front[i][j]

def move_right():
    rotate90Clockwise(cube["bottom"])
    rotate90AntiClockwise(cube["top"])
    front = deepcopy(cube["front"])
    for i in range(3):
        for j in range(3):
            cube["front"][i][j] = cube["left"][i][j]
    for i in range(3):
        for j in range(3):
            cube["left"][i][j] = cube["back"][i][j]
    for i in range(3):
        for j in range(3):
            cube["back"][i][j] = cube["right"][i][j]
    for i in range(3):
        for j in range(3):
            cube["right"][i][j] = front[i][j]
    
def update_cube(movement): 
    if(movement == "FL"): #Front Left
        move_front_left()
    
    elif(movement == "FR"): #Front Right
        move_front_right()

    elif(movement == "DN"): #Cube Down
        move_down()

    elif(movement == "UP"): #Cube Up
        move_up()

    elif(movement == "LEFT"): #Cube Left
        move_left()

    elif(movement == "RIGHT"): #Cube Right
        move_right()

    elif(movement == "TL"): #Top Left
        move_down()
        move_front_right()
        move_up()

    elif(movement == "TR"): #Top Right
        move_down()
        move_front_left()
        move_up()

    elif(movement == "RU"): #Right Up
        move_left()
        move_front_right()
        move_right()

    elif(movement == "RD"): #Right Down
        move_left()
        move_front_left()
        move_right()

    elif(movement == "LU"): #Left Up
        move_right()
        move_front_left()
        move_left()

    elif(movement == "LD"): #Left Down
        move_right()
        move_front_right()
        move_left()

    elif(movement == "BL"): #Bottom Left
        move_up()
        move_front_left()
        move_down()
        
    elif(movement == "BR"): #Bottom Right
        move_up()
        move_front_right()
        move_down()

    elif(movement == "CLOCK"): #Rotate cube 90 degree clock wise
        move_down()
        move_right()
        move_up()


    elif(movement == "ANTICLOCK"): #Rotate cube 90 degree anti clock wise
        move_down()
        move_left()
        move_up()

    else:
        print("Incorrect movement")

        
def print_cube():
    print("\t\t\t",cube["top"][0])
    print("\t\t\t",cube["top"][1])
    print("\t\t\t",cube["top"][2])
    print("\n")
    print(cube["left"][0],"\t",cube["front"][0],"\t",cube["right"][0],"\t",cube["back"][0])
    print(cube["left"][1],"\t",cube["front"][1],"\t",cube["right"][1],"\t",cube["back"][1])
    print(cube["left"][2],"\t",cube["front"][2],"\t",cube["right"][2],"\t",cube["back"][2])
    print("\n")
    print("\t\t\t",cube["bottom"][0])
    print("\t\t\t",cube["bottom"][1])
    print("\t\t\t",cube["bottom"][2])
    