### Business Analytics A - Use Case
**[...back to use case list](/../../blob/main/README.md)**

# 003 - Plane Close Crash Detector
**Summary**: Realtime visualization and detection of "close to crash approximations"
of airplanes in a defined area/region.

### 1. Use Case Classification
**Complexity:**  medium complex use case with focus on realtime-data
processing of external data, visualization of geo data. 

**Challenges:** Web data processing, map visualization, mathematical
calculation of geo data.

**Team setup:** 2 to 3 students.

### 2. Story
>Both optimists and pessimists contribute to the society. 
>The optimist invents the aeroplane, the pessimist the parachute.! 

**Me:** *I'm afraid of flying. PLanes may crash. Do they?*

**You:** *No problem, I'm a Python hero!*


### 3. Functional Requirements / Expected Results
Create a command line tool, named **planespotter.py** that... 

1. ...spins up a web server and nice web page with a map of certain area,
   displaying all the planes in that area in realtime (update frequency 
   to be defined by settings, default 5 seconds) as icons.


2. ...plane icons should point into the direction the plane is flying 
   and should show a vector pointing in the direction the plane is flying.
   The length of the vector should be defined by the current speed of the
   plane and should represent the distance the plain will fly in one minute. 
   

3. ...when two planes get too close to each other (minimum distances are 
   defined by international rules) these planes should be marked "red" as
   "close crash approximation" and warning should be shown.


4. ...as for each plane altitude, speed and direction are given,
   a prediction should be given which planes might end up in a "close 
   crash approximation" and marked as "yellow".

   
5. ...the command line tool takes the following arguments for configuration.
   
   **location**, either as an address or a city, region or country name or 
   longitude and latitude positioning (default value: Current location of 
   the computer).
   
   **radius** for the radius around the location in kilometers (default 
   value: 100km).
   
   **update** update frequency in seconds (default 5 sec).
   
   Samples for valid calls
   - **planespotter.py**
   - **planespotter.py --location "Paris"**
   - **planespotter.py --location "Silicon Valley" --radius 500**
   - **planespotter.py --location "D??sseldorf" --radius 100 --update 10**
   - **planespotter.py --long 51.246839 --lat 6.7916647 --radius 100**


3. ...supports for a help function to advice users on tool usage by entering 
   **'planespotter.py /help'** or ** 'planespotter.py /h'** on Windows or respective
   **'planespotter.py --help'** or  ** 'planespotter.py --h'** on MAc/Unix.
   

### 4. Success Criteria
A GitHub repository (public or private) that everyone can clone/download and that
directly starts up after the requirements listed in ***requirements.txt*** are fulfilled.

### 5. To get you started...
- Distance rules for planes: https://www.baatraining.com/how-close-can-a-plane-fly-to-another-aircraft
- Web and API development with Python: https://flask.palletsprojects.com/  


