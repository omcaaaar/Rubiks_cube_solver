from copy import deepcopy
import utils
import algorithm
import visualizer
    
if __name__ == "__main__":
    scan = input("Do you want to scan the faces ? y/n\nIf not, you can enter the cube faces manually in utils.py\n")
    if('y' == scan or 'Y' == scan):
    #calibrating the cube
        colors_range = visualizer.calibration()
    #scanning faces
        utils.cube = visualizer.scan_faces(colors_range)
    else:
        utils.init()
    
    cube_init = deepcopy(utils.cube)
    g_movements = algorithm.cube_solver(utils.cube)
    utils.cube = cube_init
    
    visualizer.show_movements(cube_init, g_movements)
    