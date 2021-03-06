# Rubiks_cube_solver
This repo helps you solve a 3x3x3 Rubik's cube.

## Running instructions:

1. clone the repository: 
```
git clone https://github.com/omcaaaar/Rubiks_cube_solver.git
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Run the python file ```python main.py```

Now there are two options. You can either scan the faces of your shuffled cube or you can enter the cube faces manually in utils.py.

If you opt for scanning the faces using webcam, You'll first have to calibrate the cube so that we can recognize the colors accurately based on the surrounding lighting condition.
Follow the instructions on the screen to calibrate.

Once the calibration is done, place the cube in the window shown on the screen for scanning the faces. Follow the instructions on the screen for scanning.

**Tip: Prefer standard way of holding the cube. i.e front: Red, right: blue, top: white**

**Note: Make sure the color values shown on the small cube boxes are correct before scanning the next face. If the color values are coming out to be incorrect, try to tilt the cube or change the position a little bit and press 'c'. If the issue persists, kindly consider recalibrating the cube.**

Once scanning is done, perform the movements as per shown on the screen. Make sure the current cube posion is aligned with the one shown at the bottom right corner on the screen.

You can also record and store a video of solving the cube. Set the **record** flag to **True** in ```main.py``` Line No. 20

## Rubik's cube standard notations:

**1. ANTICLOCK** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
**2. CLOCK**&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
**3. D** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
**4. D'** &emsp;&emsp;<br>
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/ANTICLOCK.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/CLOCK.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/D.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/D'.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br><br>

**5. F** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
**6. F'** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
**7. L** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
**8. L'** <br>
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/F.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/F'.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/L.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/L'.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br><br>

**9. R** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
**10. R'** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
**11. U** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
**12. U'** <br>
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/R.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/R'.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/U.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/U'.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br><br>

**13. RIGHT** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
**14. LEFT** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
**15. UP** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
**16. DOWN** <br>
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/RIGHT.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/LEFT.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/UP.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/DOWN.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br><br>

## Teaser:

![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/cube.gif)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br><br>
