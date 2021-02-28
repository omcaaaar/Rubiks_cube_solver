# Rubiks_cube_solver
This repo helps you solve a 3x3x3 Rubik's cube

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

Now there are two options. You can either scan the faces of your shuffled cube or you can enter the cube faces in utils.py.

If you opt for scanning the faces using webcam, You'll first have to calibrate the cube so that we can detect the colors accurately based on the surrounding lighting condition.
Follow the instructions on screen to calibrate.

Once the calibration is done, Place the cube in the window shown on the screen for scanning the faces. Follow the instructions on screen for scanning.

**Note: Make sure the color values shown on the small cube boxes are correct before scanning the next face. If the color values are coming out to be incorrect, try to tilt the cube or change the position a little bit and press 'c'. If the issue persists, kindly consider recalibrating the cube.**

Once scanning is done, perform the movements as per shown on the screen. Make sure the current cube posion is aligned with the one shown at the bottom right corner on the screen.

## Movements convention:

**1. ANTICLOCK:** &emsp;&emsp;**2. CLOCK:** &emsp;&emsp;&emsp;&emsp;**1. D:** &emsp;&emsp;&emsp;&emsp;&emsp;**1. D':** &emsp;&emsp;<br><br>
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/ANTICLOCK.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/CLOCK.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/D.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
![alt_text](https://github.com/omcaaaar/Rubiks_cube_solver/blob/main/assets/D'.png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
