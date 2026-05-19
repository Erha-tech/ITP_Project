# ITP_Project
ITP2_Final_Project
# Project Ansar Mansur Yerkhan

A fast-paced 2D arcade game built with Python and Tkinter where players navigate a spaceship through a procedurally generated asteroid field. 

## Features

* **Game Loop:** Handles input, coordinates physics, and manages rendering at ~33 FPS via Tkinter's event loops.
* **OOP Architecture:** Clean class structure utilizing inheritance from a base `GameObject` class.
* **Procedural Generation:** Uses trigonometric functions and randomized noise to generate unique asteroid shapes dynamically.
* **Parallax Background:** Multi-layered starfield simulation where different sized stars move at varying speeds to create depth.
* **Data Persistence:** Saves and loads global high scores locally using JSON files.
* **Dynamic Difficulty:** Scale factor that increases asteroid drop speed and spawn rates as the player's score rises.

## Technologies Used

* **Python 3.8+**
* **Tkinter** (Canvas module for vector rendering)
* **JSON** (For tracking local high scores)
* **Math & Random** (For asteroid geometry and spawn vectors)

## Installation & Running

### Prerequisites
Make sure Python 3.8 or higher is installed on your system. No external pip packages are needed.

Run the application:
python main.py


Controls
[ SPACEBAR ] — Start game from menu / Restart after Game Over.

[ LEFT ARROW ] — Move spaceship left.

[ RIGHT ARROW ] — Move spaceship right.


## Team & Contributions

Ansar (Scrum Master / Engine & UI Developer):

Designed the core application architecture based on the GameApp class.

Implemented the game state pattern (START, PLAYING, GAME_OVER), ensuring smooth screen transitions and proper memory cleanup via Canvas.delete.

Configured event-binding for macOS/Windows input systems (<Left>, <Right>, <space>).

Developed the collision detection algorithm (AABB Collision Detection) factoring in custom geometric object boundaries.

Established adaptive difficulty scaling: dynamic asteroid acceleration and spawn rate reduction as the score increases.

Erkhan (Data Handling & Quality Assurance Engineer):

Managed the execution of the Data Persistence requirement (progress tracking).

Developed the load_high_score() and save_high_score() functions for data persistence using highscore.json.

Implemented a multi-level exception handling system (Robustness) to catch json.JSONDecodeError on file corruption and IOError on access permission faults.

Conducted stress-testing to eliminate memory leaks during prolonged asteroid object generation cycles.


Mansur (Core OOP & Graphics Architect):

Implemented a deep OOP class hierarchy derived from the base GameObject class.

Programmed the complex vector rendering for the Player spaceship using 9 polygonal elements and added dynamic engine exhaust flame animations.

Utilized mathematical functions (math module and trigonometry) for procedural generation of unique asteroid shapes with randomized craters.

Applied polymorphism: the update() method behaves uniquely for obstacles (gravitational descent) and the starfield system (cosmic parallax effect with varying brightness and movement speeds).
Screenshots:

<img width="487" height="604" alt="image" src="https://github.com/user-attachments/assets/6ba2a956-5c26-4afb-a529-01e3d7983090" />

<img width="485" height="617" alt="image" src="https://github.com/user-attachments/assets/8c935894-e62a-48cf-91b4-4e65857a87f3" />

