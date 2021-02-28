import numpy as np
from utils import *

def is_solved():
    for key in cube.keys():
        if(len(np.unique(cube[key])) != 1):
            return False
        else:
            continue
    return True

def is_step_1a_solved():
    front_edges = [cube["front"][0][1], cube["front"][1][0], cube["front"][1][2], cube["front"][2][1]]
    if (len(np.unique(front_edges)) == 1):
        if(front_edges[0] == cube["back"][1][1]):
            return True
    return False

def step_1a(g_movements):   
    front_color = cube["front"][1][1]
    back_color = opp_sides[front_color]
    while(True):
        if(is_step_1a_solved()):
            break
            return True
        else:
            # getting the location of back_color edge cubies at the back side
            while(True):
                if(back_color in [cube["back"][0][1], cube["back"][1][0], cube["back"][1][2], cube["back"][2][1]]):
                    if(cube["back"][0][1] == back_color):
                        if(cube["front"][0][1] != back_color):
                            moves = ["TR", "TR"]
#                             print(moves)
                            g_movements+=moves
                            for i in moves:
                                update_cube(i)
#                             wait_key()
                            
                        else:
                            if(cube["front"][1][0] != back_color):
                                moves = ["RIGHT", "LD", "FR", "FR", "LEFT"]
#                                 print(moves)
                                g_movements+=moves
                                for i in moves:
                                    update_cube(i)
#                                 wait_key()
                            elif(cube["front"][1][2] != back_color):
                                moves = ["LEFT", "RD", "FR", "FR", "RIGHT"]
#                                 print(moves)
                                g_movements+=moves
                                for i in moves:
                                    update_cube(i)
#                                 wait_key()
                            elif(cube["front"][2][1] != back_color):
                                moves = ["LEFT", "RD", "RD", "BL", "BL", "RIGHT"]
#                                 print(moves)
                                g_movements+=moves
                                for i in moves:
                                    update_cube(i)
#                                 wait_key()
                    else:
#                         print("CLOCK")
                        g_movements.append("CLOCK")
                        update_cube("CLOCK")
#                         wait_key()
                else:
                    break

            # moving side edge cubies
            while(True):
                if(back_color in [cube["top"][0][1], cube["top"][1][0], cube["top"][1][2], cube["top"][2][1]
                            ,cube["right"][0][1], cube["right"][1][0], cube["right"][1][2], cube["right"][2][1]
                            ,cube["left"][0][1], cube["left"][1][0], cube["left"][1][2], cube["left"][2][1]
                            ,cube["bottom"][0][1], cube["bottom"][1][0], cube["bottom"][1][2], cube["bottom"][2][1]]):
                    count = 0
                    if(back_color in [cube["left"][0][1], cube["left"][1][0], cube["left"][1][2], cube["left"][2][1]]):
                        for l_rot in range(4):
                            if(cube["left"][0][1] == back_color):
                                for fr_rot in range(4):
                                    if(cube["front"][0][1] != back_color):
#                                         print("TR")
                                        g_movements.append("TR")
                                        update_cube("TR")
#                                         wait_key()
                                        count+=1
                                        break
                                    else:
#                                         print("FR")
                                        g_movements.append("FR")
                                        update_cube("FR")
#                                         wait_key()
                                if(count != 0):
                                    break
                            else:
#                                 print("LD")
                                g_movements.append("LD")
                                update_cube("LD")
#                                 wait_key()
                        
                    else:
#                         print("CLOCK")
                        g_movements.append("CLOCK")
                        update_cube("CLOCK")
#                         wait_key()
                else:
                    break

def is_step_1b_solved():
    back_edges = [cube["back"][0][1], cube["back"][1][0], cube["back"][1][2], cube["back"][2][1]]
    if (len(np.unique(back_edges)) == 1):
        if(back_edges[0] == cube["back"][1][1]):
            return True
    return False    

def step_1b(g_movements):
    front_color = cube["front"][1][1]
    back_color = opp_sides[front_color]
    while(True):
        count = 0
        if(back_color in [cube["front"][0][1], cube["front"][1][0], cube["front"][1][2], cube["front"][2][1]]):
            for fr_rot1 in range(4):
                if(cube["front"][0][1] == back_color):
                    for fr_rot2 in range(4):
                        if(cube["top"][1][1] == cube["top"][2][1]):
                            moves = ["TR", "TR"]
#                             print(moves)
                            g_movements+=moves
                            for i in moves:
                                update_cube(i)
#                             wait_key()
                            count+=1
                            break
                        else:
                            moves = ["FR", "ANTICLOCK"]
#                             print(moves)
                            g_movements+=moves
                            for i in moves:
                                update_cube(i)
#                             wait_key()
                    if(count!=0):
                        break
                else:
#                     print("CLOCK")
                    g_movements.append("CLOCK")
                    update_cube("CLOCK")
#                     wait_key()
        else:
            break
#     if(is_step_1b_solved()):
#         print("step 1b completed")
#         print_cube()

def is_step_1c_solved():
    if(len(np.unique(cube["front"])) == 1 and cube["front"][0][0] == cube["front"][1][1]):
        if(cube["top"][2][1] == cube["top"][1][1] and cube["right"][1][0] == cube["right"][1][1] and cube["left"][1][2] == cube["left"][1][1] and cube["bottom"][0][1] == cube["bottom"][1][1]):
            if(cube["top"][2][0] == cube["top"][1][1] and cube["top"][2][2] == cube["top"][1][1] and 
              cube["right"][0][0] == cube["right"][1][1] and cube["right"][2][0] == cube["right"][1][1] and
              cube["left"][0][2] == cube["left"][1][1] and cube["left"][2][2] == cube["left"][1][1] and 
              cube["bottom"][0][0] == cube["bottom"][1][1] and cube["bottom"][0][2] == cube["bottom"][1][1]):
                return True
    return False



def step_1c(g_movements):
    # now considering back side as front
    moves = ["DN", "DN"]
#     print(moves)
    g_movements+=moves
    for i in moves:
        update_cube(i)
#     wait_key()
    front_color = cube["front"][1][1]
    while(True):
        if(is_step_1c_solved()):
            return True
        else:
            while(True):
                if(front_color in [cube["top"][0][0], cube["top"][0][2], cube["right"][0][2], cube["right"][2][2], cube["left"][0][0], cube["left"][2][0], cube["bottom"][2][0], cube["bottom"][2][2]]):
                    if(front_color == cube["top"][0][0] or front_color == cube["top"][0][2]):
                        if(front_color == cube["top"][0][0]):
                            for t_rot2 in range(4):
                                if(cube["left"][0][0] == cube["left"][1][1]):
                                    moves = ["TL", "RIGHT", "LD", "TR", "LEFT"]
#                                     print(moves)
                                    g_movements+=moves
                                    for i in moves:
                                        update_cube(i)
#                                     wait_key()
                                    break
                                    
                                else:
                                    moves = ["DN", "TR", "LEFT", "UP"]
#                                     print(moves)
                                    g_movements+=moves
                                    for i in moves:
                                        update_cube(i)
#                                     wait_key()
                            else:
                                print("something went wrong")
                                print_cube()
                                return False


                        if(front_color == cube["top"][0][2]):
                            for t_rot2 in range(4):
                                if(cube["right"][0][2] == cube["right"][1][1]):
                                    moves = ["TR", "LEFT", "RD", "TL", "RIGHT"]
#                                     print(moves)
                                    g_movements+=moves
                                    for i in moves:
                                        update_cube(i)
#                                     wait_key()
                                    # print_cube()
                                    break
                                else:
                                    moves = ["DN", "TR", "LEFT", "UP"]
#                                     print(moves)
                                    g_movements+=moves
                                    for i in moves:
                                        update_cube(i)
#                                     wait_key()
                            else:
                                print("something went wrong")
                                return False
                    else:
                        moves = ["DN", "TR", "UP"]
#                         print(moves)
                        g_movements+=moves
                        for i in moves:
                            update_cube(i)
#                         wait_key()
                else:
                    break
            
            count2 = 0
            if(front_color in [cube["back"][0][0], cube["back"][0][2], cube["back"][2][0], cube["back"][2][2]]):
                count1 = 0
                count2+=1
                for clk1 in range(4):
                    if(front_color in cube["back"][0][0]):
                        for clk2 in range(4):
                            if(front_color == cube["front"][0][2] and cube["top"][2][2] == cube["top"][1][1] and cube["right"][0][0] == cube["right"][1][1]):
                                moves = ["DN", "TR", "LEFT", "UP"]
#                                 print(moves)
                                g_movements+=moves
                                for i in moves:
                                    update_cube(i)
#                                 wait_key()
                            else:   
                                moves = ["DN", "RU", "TL", "TL", "RD", "UP"]
#                                 print(moves)
                                g_movements+=moves
                                for i in moves:
                                    update_cube(i)
#                                 wait_key()
                                count1+=1
                                break
                        if(count1!=0):
                            break
                    else:
#                         print("CLOCK")
                        g_movements.append("CLOCK")
                        update_cube("CLOCK")
#                         wait_key()

            count3 = 0
            if(count2 == 0):
#                 count3+=1
                if(front_color in [cube["top"][2][0], cube["top"][2][2], cube["right"][0][0], cube["right"][2][0], cube["bottom"][0][0], cube["bottom"][0][2], cube["left"][0][2], cube["left"][2][2]]):
                    count3+=1
                    for clk in range(4):
                        if(front_color in [cube["top"][2][2], cube["right"][0][0]]):
                            moves = ["RU", "DN", "TL", "RD", "UP"]
#                             print(moves)
                            g_movements+=moves
                            for i in moves:
                                update_cube(i)
#                             wait_key()
                            break
                        else:
#                             print("CLOCK")
                            g_movements.append("CLOCK")
                            update_cube("CLOCK")
#                             wait_key()

            if(count3 == 0):
                for clk in range(4):
                    if(front_color == cube["front"][0][2]):
                        if(cube["top"][2][2] == cube["top"][1][1] and cube["right"][0][0] == cube["right"][1][1]):
#                           print("CLOCK")
                            g_movements.append("CLOCK")
                            update_cube("CLOCK")
#                           wait_key()
                            continue
                        else:
                            moves = ["RU", "DN", "TL", "RD", "UP"]
#                             print(moves)
                            g_movements+=moves
                            for i in moves:
                                update_cube(i)
#                             wait_key()
                            break
                    else:
#                         print("CLOCK")
                        g_movements.append("CLOCK")
                        update_cube("CLOCK")
#                         wait_key()

def layer_1(g_movements):
    step_1a(g_movements)
    step_1b(g_movements)
    step_1c(g_movements)
#     if(is_step_1c_solved()):
#         print("Layer 1 solved")
#         print_cube()

def is_layer_2_solved():
    faces = ["front", "left", "right", "back"]
    for face in faces:
        face_color = cube[face][1][1]
        if(face_color == cube[face][1][0] and face_color == cube[face][1][2]):
            continue
        else:
            return False
#     print("layer 2 solved")
#     print_cube()
    return True
            

def layer_2(g_movements):
    # moving front layer (layer 1) to top
#     print("UP")
    g_movements.append("UP")
    update_cube("UP")
#     wait_key()

    while(True):
        if(is_layer_2_solved()):
            return True
        else:
            while(True):
                bottom_color = cube["bottom"][1][1]
                bottom_edges_color = [(cube["bottom"][0][1], cube["front"][2][1]), (cube["bottom"][1][0], cube["left"][2][1]), 
                                        (cube["bottom"][1][2], cube["right"][2][1]), (cube["bottom"][2][1], cube["back"][2][1])]
                
                edge_flag = 0
                for edge in range(4):
                    if(bottom_color in bottom_edges_color[edge]):
                        continue
                    else:
                        edge_flag+=1

                if(edge_flag != 0):
                    if(cube["front"][2][1] != cube["bottom"][1][1] and cube["bottom"][0][1] != cube["bottom"][1][1]):
                        for rot in range(4):
                            if(cube["front"][2][1] == cube["front"][1][1]):
                                if(cube["bottom"][0][1] == cube["left"][1][1]):
                                    moves = ["BR", "LD", "BL", "LU", "BL", "FL", "BR", "FR"]
#                                     print(moves)
                                    g_movements+=moves
                                    for i in moves:
                                        update_cube(i)
#                                     wait_key()
                                    break
                                elif(cube["bottom"][0][1] == cube["right"][1][1]):
                                    moves = ["BL", "RD", "BR", "RU", "BR", "FR", "BL", "FL"]
#                                     print(moves)
                                    g_movements+=moves
                                    for i in moves:
                                        update_cube(i)
#                                     wait_key()
                                    break
                                else:
                                    print("something went wrong")
                                    return False
                            else:
                                moves = ["BR", "LEFT"]
#                                 print(moves)
                                g_movements+=moves
                                for i in moves:
                                    update_cube(i)
#                                 wait_key()

                    else:
#                         print("LEFT")
                        g_movements.append("LEFT")
                        update_cube("LEFT")
#                         wait_key()
                else:
                    break

            layer_2_edge_colors = [(cube["front"][1][0], cube["left"][1][2]), (cube["front"][1][2], cube["right"][1][0]), 
                                    (cube["right"][1][2], cube["back"][1][0]), (cube["back"][1][2], cube["left"][1][0])]

            l2_chng_flag = 0
            for l2_ec in range(4):
                if(bottom_color in layer_2_edge_colors[l2_ec]):
                    continue
                else:
                    if(is_layer_2_solved()):
                        return True
                    l2_chng_flag+=1
            if(l2_chng_flag != 0):
                for rot in range(4):
                    if(cube["front"][1][2] != bottom_color and cube["right"][1][0] != bottom_color):
                        moves = ["BL", "RD", "BR", "RU", "BR", "FR", "BL", "FL"]
#                         print(moves)
                        g_movements+=moves
                        for i in moves:
                            update_cube(i)
#                         wait_key()
                        break
                    else:
#                         print("LEFT")
                        g_movements.append("LEFT")
                        update_cube("LEFT")
#                         wait_key()

def layer_3(g_movements):
    # getting layer 3 at top
    moves = ["UP", "UP"]
#     print(moves)
    g_movements+=moves
    for i in moves:
        update_cube(i)
#     wait_key()

    while(True):
        if(is_solved()):
            print("cube solved")
            print_cube()
            return True
        else:
            top_color = cube["top"][1][1]
            while(True):
                if(cube["top"][0][1] != top_color or cube["top"][1][0] != top_color 
                    or cube["top"][1][2] != top_color or cube["top"][2][1] != top_color):
                    for rot1 in range(3):
                        if(cube["top"][1][0] == top_color and cube["top"][1][2] == top_color):
                            moves = ["FR", "RU", "TL", "RD", "TR", "FL"]
#                             print(moves)
                            g_movements+=moves
                            for i in moves:
                                update_cube(i)
#                             wait_key()
                            break
                        else:
#                             print("LEFT")
                            g_movements.append("LEFT")
                            update_cube("LEFT")
#                             wait_key()
                    else:
                        for rot2 in range(4):
                            if(cube["top"][2][1] == top_color and cube["top"][2][2] == top_color):
                                moves = ["FR", "RU", "TL", "RD", "TR", "FL"]
#                                 print(moves)
                                g_movements+=moves
                                for i in moves:
                                    update_cube(i)
#                                 wait_key()
                                break

                            else:
#                                 print("LEFT")
                                g_movements.append("LEFT")
                                update_cube("LEFT")
#                                 wait_key()
                        else:
                            moves = ["FR", "RU", "TL", "RD", "TR", "FL"]
#                             print(moves)
                            g_movements+=moves
                            for i in moves:
                                update_cube(i)
#                             wait_key()
                else:
#                     print("break")
#                     print_cube()
                    break

            for rot1 in range(4):
                front_color = cube["front"][1][1]
                left_color = cube["left"][1][1]
                right_color = cube["right"][1][1]
                back_color = cube["back"][1][1]
                if(cube["front"][0][1] == front_color and cube["left"][0][1] == left_color and cube["right"][0][1] == right_color and cube["back"][0][1] == back_color):
#                     print("break")
#                     print_cube()
                    break
                else:
                    count1 = 0
                    for rot2 in range(4):
                        for rot3 in range(4):
                            if(cube["front"][0][1] == cube["front"][1][1] and cube["left"][0][1] == cube["left"][1][1]):
#                                 print("LEFT")
                                g_movements.append("LEFT")
                                update_cube("LEFT")
#                                 wait_key()
                                moves = ["RU", "TL", "TL", "RD", "TR", "RU", "TR", "RD", "TR"]
#                                 print(moves)
                                g_movements+=moves
                                for i in moves:
                                    update_cube(i)
#                                 wait_key()
                                # print_cube()
                                count1+=1
                                break
                            else:
#                                 print("LEFT")
                                g_movements.append("LEFT")
                                update_cube("LEFT")
#                                 wait_key()
                        if(count1 == 0):
#                             print("TR")
                            g_movements.append("TR")
                            update_cube("TR")
#                             wait_key()
                        else:
                            break
                    else:
                        moves = ["RU", "TL", "TL", "RD", "TR", "RU", "TR", "RD", "TR"]
#                         print(moves)
                        g_movements+=moves
                        for i in moves:
                            update_cube(i)
#                       wait_key()

            while(True):
                top_color = cube["top"][1][1]
                front_color = cube["front"][1][1]
                right_color = cube["right"][1][1]
                left_color = cube["left"][1][1]
                back_color = cube["back"][1][1]

                top_corner_pieces = [(cube["top"][2][2], cube["front"][0][2], cube["right"][0][0]),
                                     (cube["top"][2][0], cube["front"][0][0], cube["left"][0][2]),
                                     (cube["top"][0][0], cube["left"][0][0], cube["back"][0][2]), 
                                     (cube["top"][0][2], cube["right"][0][2], cube["back"][0][0])]

                top_corner_pos = [(top_color, front_color, right_color),
                                  (top_color, front_color, left_color), 
                                  (top_color, left_color, back_color), 
                                  (top_color, right_color, back_color)]

                # checking the position of corner pieces
                correct_count = 0
                for piece in range(4):
                    if(sorted(top_corner_pieces[piece]) == sorted(top_corner_pos[piece])):
                        correct_count+=1
                        # continue
                    # else:
                    #     break
                if(correct_count == 4):
                    # print_cube()
                    break

                if(correct_count != 0):
                    if(sorted(top_corner_pieces[0]) == sorted(top_corner_pos[0])):
                        moves = ["LU", "TL", "RU", "TR", "LD", "TL", "RD", "TR"]
#                         print(moves)
                        g_movements+=moves
                        for i in moves:
                            update_cube(i)
#                         wait_key()
                    
                    else:
#                         print("LEFT")
                        g_movements.append("LEFT")
                        update_cube("LEFT")
#                         wait_key()
                else:
                    moves = ["LU", "TL", "RU", "TR", "LD", "TL", "RD", "TR"]
#                     print(moves)
                    g_movements+=moves
                    for i in moves:
                        update_cube(i)
#                     wait_key()

            while(True):
                if(is_solved()):
                    break
                else:
                    top_color = cube["top"][1][1]
                    front_color = cube["front"][1][1]
                    right_color = cube["right"][1][1]
                    left_color = cube["left"][1][1]
                    back_color = cube["back"][1][1]

                    top_corner_pieces = [(cube["top"][2][2], cube["front"][0][2], cube["right"][0][0]),
                                        (cube["top"][2][0], cube["front"][0][0], cube["left"][0][2]),
                                        (cube["top"][0][0], cube["left"][0][0], cube["back"][0][2]), 
                                        (cube["top"][0][2], cube["right"][0][2], cube["back"][0][0])]

                    top_corner_pos = [(top_color, front_color, right_color),
                                    (top_color, front_color, left_color), 
                                    (top_color, left_color, back_color), 
                                    (top_color, right_color, back_color)]

                    if(top_corner_pieces[0] != top_corner_pos[0] and top_corner_pieces[3] != top_corner_pos[3]):
                        moves = ["RU", "TL", "TL", "RD", "TR", "RU", "TR", "RD"]
#                         print(moves)
                        g_movements+=moves
                        for i in moves:
                            update_cube(i)
#                         wait_key()
                        moves = ["LU", "TL", "TL", "LD", "TL", "LU", "TL", "LD"]
#                         print(moves)
                        g_movements+=moves
                        for i in moves:
                            update_cube(i)
#                         wait_key()

                    elif(top_corner_pieces[0] != top_corner_pos[0] and top_corner_pieces[3] == top_corner_pos[3] and
                        top_corner_pieces[2] != top_corner_pos[2] and top_corner_pieces[1] == top_corner_pos[1]):
                        moves = ["RU", "TL", "TL", "RD", "TR", "RU", "TR", "RD"]
#                         print(moves)
                        g_movements+=moves
                        for i in moves:
                            update_cube(i)
#                         wait_key()
                        moves = ["LU", "TL", "TL", "LD", "TL", "LU", "TL", "LD"]
#                         print(moves)
                        g_movements+=moves
                        for i in moves:
                            update_cube(i)
#                         wait_key()

                    else:
#                         print("LEFT")
                        g_movements.append("LEFT")
                        update_cube("LEFT")
#                         wait_key()

def cube_solver(cube_init):
    global cube, opp_sides
    global g_movements
    cube = cube_init
    opp_sides = {"Y":"W", "W":"Y",
                "B":"G", "G":"B",
                "R":"O", "O":"R"}
    g_movements = list()
    layer_1(g_movements)
    layer_2(g_movements)
    layer_3(g_movements)
    g_movements = redundant_steps_remover(g_movements)
    
    return g_movements