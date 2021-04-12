### Business Analytics A - Use Case 
# 001 - Earth Quake Detector
### 1. Use Case Classification
**Complexity:**  medium complex use case with focus on the selection and 
orchestration of various Python packages and the implementation of a frontend 
to get the job done. 

**Challenges:** Processing of real-time data, geo data calcuations and visualization, 
OpenStreetMaps, web frontend development, web-service backend development.

**Team setup:** 2 to 3 students.

### 1. Purpose
>A simple earth quake alerting system for the masses! 

**Me:** *I'm looking for real good vibrations! Where are they?*

**You:** *No problem, I'm a Python hero!*


### 2. Functional Requirements / Expected Results
Create a command line tool, named **quakemonitor.py** that... 

1. ...starts a web server, opens a web page in the default browser that provides the
   following features:
   - A nice logo and layout. Use the HSD logo or create your own.
   - A Google-like search field at the top with a search button to update the 
     visualization. The field should be prefilled with the current location.
     Pressing the search button will read the location from the search field
     and refresh the page.
   - Below the search field a screen-filling map is shown with the selected location
     in the center, and a zoom-in factor appropriate to cover a circle with actual 
     search radius.
   - On overlay that draws the location of all earthquakes of the last 24 hours 
     into the actual map, represented by a circle contains the strength (Richter scala)
     of the earth quake and a label with the timestamp of the earth quake.
   - the web page should be update evers


2. ...the command line tool takes two arguments for configuration, a location
   either as an address or a city, region or country name or longitude and latitude
   positioning (default value: Current location of the computer), a radius 
   for the radius around the location in kilometers (default value: 250km) and
   an update frequency in seconds (default 30 sec) . 
   Samples for valid calls
   - **quakemonitor.py**
   - **quakemonitor.py --location "Paris"**
   - **quakemonitor.py --location "Silicon Valley" --radius 500**
   - **quakemonitor.py --location "Düsseldorf" --radius 100 --update 10**
   - **quakemonitor.py --long 51.246839 --lat 6.7916647 --radius 100**


### 3. Success Criteria
A GitHub repository (public or private) that everyone can clone/download and that
directly starts up after the requirements listed in ***requirements.txt*** are fulfilled.


### 4. To get you started...
 - Flask for backend and webserver: https://flask.palletsprojects.com/en/1.1.x/
 - OSM & Overpass: https://towardsdatascience.com/loading-data-from-openstreetmap-with-python-and-the-overpass-api-513882a27fd0
 - OSM Wiki: https://wiki.openstreetmap.org/wiki/Main_Page
 -  


