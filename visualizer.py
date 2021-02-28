import numpy as np
import cv2
from utils import update_cube

std_notations = {"FL": "F'", "FR":"F", "DN":"DOWN", "UP":"UP", "LEFT":"LEFT", "RIGHT":"RIGHT", 
                 "TL":"U", "TR":"U'", "RU": "R", "RD":"R'", "LU":"L'", "LD":"L", "BL":"D'", "BR":"D",
                "CLOCK":"CLOCK", "ANTICLOCK":"ANTICLOCK", "CUBE SOLVED":"CUBE SOLVED"}

def scan_faces(colors_range):
    ret_dict = dict()
    faces = ["front", "right", "back", "left", "top", "bottom"]
    for face in faces:
        ret_dict[face] = [[0,0,0], [0,0,0], [0,0,0]]
    face_iter = iter(faces)
    
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (10, 50) 
    fontScale = 0.5
    color = (255, 0, 0) 
    thickness = 2
    
    cap = cv2.VideoCapture(0)
    ret=True
    face = next(face_iter)
    while(ret):
        ret,im = cap.read()
        im = cv2.flip(im, 1)
        frame_width = int(round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
        frame_height = int(round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        
        top_left = (int(frame_width/3), int(frame_height/3))
        pcs_width = int(0.05*frame_width)
        gap = pcs_width
        start_pts = [(top_left[0]+(0.5*gap), top_left[1]+(0.5*gap))]
        
        im = draw_cube_boundry(im, frame_width, frame_height)
        im = cv2.putText(im, 'Scanning faces... Please show '+face+' face :: press c to capture', org, font,  
                       fontScale, color, thickness, cv2.LINE_AA)
        im = cv2.putText(im, 'if capturing is done properly, press n for the next face, press c to recapture', 
                         (org[0], org[1]+20), font, fontScale, color, thickness, cv2.LINE_AA)
        

        for h in range(3):
            for w in range(3):
                next_start_w = int(start_pts[0][0]+(gap*w*2))
                next_start_h = int(start_pts[0][1]+(gap*h*2))
                im = cv2.putText(im, str(ret_dict[face][h][2-w]), (int(next_start_w+(gap/2)), int(next_start_h+(gap/2))), font,  
                       fontScale, (0,0,0), 1, cv2.LINE_AA)
        cv2.imshow("frame",im)
        pressedKey = cv2.waitKey(1) & 0xFF
        if pressedKey == ord('c'):
            for h in range(3):
                for w in range(3):
                    next_start_w = int(start_pts[0][0]+(gap*w*2))
                    next_start_h = int(start_pts[0][1]+(gap*h*2))
                    
                    piece_val = cv2.mean(im[next_start_h:next_start_h+gap, next_start_w:next_start_w+gap])[:3]
                    min_dist = np.Inf
                    for key in colors_range.keys():
                        clr_range = colors_range[key]
                        dist = abs(piece_val[0]-clr_range[0]) + abs(piece_val[1]-clr_range[1]) + abs(piece_val[2]-clr_range[2])
                        if(dist<min_dist):
                            min_dist = dist
                            ret_dict[face][h][2-w] = key[0]
                            
        if pressedKey == ord('n'):    
            try:
                face = next(face_iter)
            except:
                break
                
        if pressedKey == ord('q'):
            break
                
    cap.release()
    cv2.destroyAllWindows()
    return ret_dict


def calibration():
    ret_dict =dict()
    colors = ["WHITE", "ORANGE", "RED", "YELLOW", "GREEN", "BLUE"]
    clr_iter = iter(colors)
    
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (50, 50) 
    fontScale = 0.5
    color = (255, 0, 0) 
    thickness = 2
        
    cap = cv2.VideoCapture(0)
    ret=True
    clr = next(clr_iter)
    while(ret):
        ret,im = cap.read()
        frame_width = int(round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
        frame_height = int(round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        
        top_left = (int(frame_width/3), int(frame_height/3))
        pcs_width = int(0.05*frame_width)
        gap = pcs_width
        start_pts = [(top_left[0]+(0.5*gap), top_left[1]+(0.5*gap))]

        start_loc = (int(start_pts[0][0]+(2*gap)), int(start_pts[0][1]+(2*gap)))
        end_loc = (int(start_loc[0]+gap), int(start_loc[1]+gap))
    
        im = cv2.flip(im, 1)
        im = draw_cube_boundry_calibration(im, frame_width, frame_height)
        
        im = cv2.putText(im, 'Calibrating cube... Please show '+clr+' color :: press c to continue', org, font,  
                       fontScale, color, thickness, cv2.LINE_AA)
        
        cv2.imshow('frame',im)
        
        
        pressedKey = cv2.waitKey(1) & 0xFF
        if pressedKey == ord('c'):
            ret_dict[clr] = cv2.mean(im[start_loc[1]:start_loc[1]+gap,start_loc[0]:start_loc[0]+gap])[:3]
            try:
                clr = next(clr_iter)
            except:
                break
                
        if pressedKey == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    return ret_dict


def draw_cube_boundry(image, frame_width, frame_height):
    top_left = (int(frame_width/3), int(frame_height/3))
    pcs_width = int(0.05*frame_width)
    gap = pcs_width
    bottom_right = (top_left[0]+6*gap, top_left[1]+6*gap)
    color = (255,0,0)
    thickness = 2
    
    cv2.rectangle(image, top_left, bottom_right, color, thickness)
    
    start_pts = [(top_left[0]+(0.5*gap), top_left[1]+(0.5*gap))]
    for h in range(3):
        for w in range(3):
            next_start_w = int(start_pts[0][0]+(gap*w*2))
            next_start_h = int(start_pts[0][1]+(gap*h*2))
            
            next_end_w = next_start_w+gap
            next_end_h = next_start_h+gap
            
            cv2.rectangle(image, (next_start_w, next_start_h), (next_end_w, next_end_h), color, thickness)
            
    return image

def draw_cube_boundry_calibration(image, frame_width, frame_height):
    top_left = (int(frame_width/3), int(frame_height/3))
    pcs_width = int(0.05*frame_width)
    gap = pcs_width
    color = (255,0,0)
    thickness = 2
    
    start_pts = [(top_left[0]+(0.5*gap), top_left[1]+(0.5*gap))]
    
    next_start_w = int(start_pts[0][0]+(gap*2))
    next_start_h = int(start_pts[0][1]+(gap*2))

    next_end_w = next_start_w+gap
    next_end_h = next_start_h+gap

    cv2.rectangle(image, (next_start_w, next_start_h), (next_end_w, next_end_h), color, thickness)
            
    return image

def draw_animation(image, move):
    COLORS = {"W": (255,255,255), "B":(255,0,0), "R":(0,0,255), "G":(0,255,0), "O":(0,165,255), "Y":(0,255,255)}
    black_color = (0,0,0)
    frame_width = image.shape[1]
    frame_height = image.shape[0]
    gap = int(0.075*frame_width)
    
    top_start_w = 50
    top_start_h = 100
    
    image = cv2.putText(image, "FRONT", (int(top_start_w+gap),int(top_start_h+3.5*gap)), cv2.FONT_HERSHEY_SIMPLEX ,  
                   0.5, (0,0,0), 2, cv2.LINE_AA)
    
    for h in range(3):
        for w in range(3):
            rect_start_w = int(top_start_w+w*gap)
            rect_start_h = int(top_start_h+h*gap)
            rect_end_w = int(rect_start_w+gap)
            rect_end_h = int(rect_start_h+gap)
            image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), 
                                  COLORS[cube["front"][h][w]], -1, cv2.LINE_8)
            image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), black_color, 2)
            
    if(move=="CLOCK"):
        image = cv2.circle(image, (int(top_start_w+1.5*gap), int(top_start_h+1.5*gap)), gap, black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
    elif(move=="ANTICLOCK"):
        image = cv2.circle(image, (int(top_start_w+1.5*gap), int(top_start_h+1.5*gap)), gap, black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        
    elif(move=="FL"):
        image = cv2.arrowedLine(image, (int(top_start_w+1.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+1.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+1.5*gap)), 
                                (int(top_start_w+1.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+1.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+1.5*gap)), 
                                     black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+1.5*gap)), 
                                (int(top_start_w+1.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
    elif(move=="FR"):
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+1.5*gap)), 
                                (int(top_start_w+1.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+1.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+1.5*gap)), 
                                     black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+1.5*gap)), 
                                (int(top_start_w+1.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        image = cv2.arrowedLine(image, (int(top_start_w+1.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+1.5*gap)), 
                                     black_color, 1)
        
    elif(move=="DN"):
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+1.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+1.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        
    elif(move=="UP"):
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+1.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+1.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
    elif(move=="LEFT"):
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+1.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+1.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        
    elif(move=="RIGHT"):
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+1.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+1.5*gap)), 
                                     black_color, 1)
        
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        
    elif(move=="TL"):
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
    elif(move=="TR"):
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
    elif(move=="RU"):
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
    elif(move=="RD"):
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        
    elif(move=="LU"):
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                     black_color, 1)
        
    elif(move=="LD"):
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+0.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        
    elif(move=="BL"):
        image = cv2.arrowedLine(image, (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        
    elif(move=="BR"):
        image = cv2.arrowedLine(image, (int(top_start_w+0.5*gap), int(top_start_h+2.5*gap)), 
                                (int(top_start_w+2.5*gap), int(top_start_h+2.5*gap)), 
                                     black_color, 1)
        
    return image
            
def draw_cube(image, move):
    COLORS = {"W": (255,255,255), "B":(255,0,0), "R":(0,0,255), "G":(0,255,0), "O":(0,165,255), "Y":(0,255,255)}
    black_color = (0,0,0)
    frame_width = image.shape[1]
    frame_height = image.shape[0]
    gap = int(0.025*frame_width)
    
    image = draw_animation(image, move)
    
    image = cv2.putText(image, "next move: "+std_notations[move] , (50,50), cv2.FONT_HERSHEY_SIMPLEX ,  
                   1, (255,0,0), 2, cv2.LINE_AA)
    
    image = cv2.putText(image, "current cube position: ", (int(frame_width*0.55),int(frame_height*0.5)), cv2.FONT_HERSHEY_SIMPLEX ,  
                   0.75, (255,0,0), 2, cv2.LINE_AA)
    
    top_start_w = int(frame_width*0.6 + 4*gap)
    top_start_h = int(frame_height*0.55)
    middle_start_w = int(frame_width*0.6)
    middle_start_h = int(frame_height*0.55 + 4*gap)
    bottom_start_w = int(frame_width*0.6 + 4*gap)
    bottom_start_h = int(frame_height*0.55 + 8*gap)
    
    image = cv2.putText(image, "top", (int(top_start_w+3.5*gap),int(top_start_h+1.5*gap)), cv2.FONT_HERSHEY_SIMPLEX ,  
                   0.5, (0,0,0), 1, cv2.LINE_AA)
    image = cv2.putText(image, "left", (int(middle_start_w+0.5*gap), int(middle_start_h-0.25*gap)), cv2.FONT_HERSHEY_SIMPLEX ,  
                   0.5, (0,0,0), 1, cv2.LINE_AA)
    image = cv2.putText(image, "front", (int(middle_start_w+4.5*gap),int(middle_start_h-0.25*gap)), cv2.FONT_HERSHEY_SIMPLEX ,  
                   0.5, (0,0,0), 1, cv2.LINE_AA)
    image = cv2.putText(image, "right", (int(middle_start_w+8.5*gap),int(middle_start_h-0.25*gap)), cv2.FONT_HERSHEY_SIMPLEX ,  
                   0.5, (0,0,0), 1, cv2.LINE_AA)
    image = cv2.putText(image, "back", (int(middle_start_w+12.5*gap),int(middle_start_h-0.25*gap)), cv2.FONT_HERSHEY_SIMPLEX ,  
                   0.5, (0,0,0), 1, cv2.LINE_AA)
    image = cv2.putText(image, "bottom", (int(bottom_start_w+3.5*gap),int(bottom_start_h+1.5*gap)), cv2.FONT_HERSHEY_SIMPLEX ,  
                   0.5, (0,0,0), 1, cv2.LINE_AA)
    
    #for top level
    for h in range(3):
        for w in range(3):
            rect_start_w = int(top_start_w+w*gap)
            rect_start_h = int(top_start_h+h*gap)
            rect_end_w = int(rect_start_w+gap)
            rect_end_h = int(rect_start_h+gap)
            
            image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), 
                                  COLORS[cube["top"][h][w]], -1, cv2.LINE_8)
            image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), black_color, 1)
            
    #for middle level
    for h in range(3):
        for w in range(15):
            rect_start_w = int(middle_start_w+w*gap)
            rect_start_h = int(middle_start_h+h*gap)
            rect_end_w = int(rect_start_w+gap)
            rect_end_h = int(rect_start_h+gap)
            if(w==3 or w==7 or w==11):
                continue
            if(w<3):
                image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), 
                                  COLORS[cube["left"][h][w]], -1, cv2.LINE_8)
                image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), black_color, 1)
                
            elif(w<7 and w>3):
                image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), 
                                  COLORS[cube["front"][h][w-4]], -1, cv2.LINE_8)
                image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), black_color, 1)
                
            elif(w<11 and w>7):
                image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), 
                                  COLORS[cube["right"][h][w-8]], -1, cv2.LINE_8)
                image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), black_color, 1)
            elif(w<15 and w>11):
                image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), 
                                  COLORS[cube["back"][h][w-12]], -1, cv2.LINE_8)
                image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), black_color, 1)
                
    #for bottom level
    for h in range(3):
        for w in range(3):
            rect_start_w = int(bottom_start_w+w*gap)
            rect_start_h = int(bottom_start_h+h*gap)
            rect_end_w = int(rect_start_w+gap)
            rect_end_h = int(rect_start_h+gap)
            
            image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), 
                                  COLORS[cube["bottom"][h][w]], -1, cv2.LINE_8)
            image = cv2.rectangle(image, (rect_start_w,rect_start_h), (rect_end_w,rect_end_h), black_color, 1)
            
            
    return image


def show_movements(cube_init, g_movements, record=False, video_path='./cube.mp4'):
    global cube 
    cube = cube_init
#     print(cube)
    if(record):
        out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*"MP4V"), 30, (640, 480))

    g_movements_iter = iter(g_movements)
    cap = cv2.VideoCapture(0)
    ret=True
    move = next(g_movements_iter)
    is_solved = 0
    while(ret):
        ret,im = cap.read()
        width = int(round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
        height = int(round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        fps = cap.get(cv2.CAP_PROP_FPS)
    #     print(fps)
        im = cv2.flip(im, 1)

        im = draw_cube(im, move)

        pressedKey = cv2.waitKey(1) & 0xFF
        if pressedKey == ord('c'):
            try:
                if(is_solved == 0):
                    update_cube(move)
                    move = next(g_movements_iter)
                else:
                    move = "CUBE SOLVED"
            except:
                move = "CUBE SOLVED"
                is_solved = 1
    #             break

        if pressedKey == ord('q'):
            break

        cv2.imshow('frame0',im)
        if(record):
            out.write(im)

    if(record):
        out.release()
    cap.release()
    cv2.destroyAllWindows()