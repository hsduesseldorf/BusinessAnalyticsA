### Business Analytics A - Use Case
**[...back to use case list](/../../blob/main/README.md)**

# 010 - Night Time Noise and Snoring Tracker and Recorder
**Complexity:** Implement a sleeping and snoring tracker in Python
that monitors, analyses and logs any relevant noise over the night.
### 1. Use Case Classification
**Complexity:**  medium complex use case with focus on sensor data  
analysis and real-time data processing. 

**Challenges:** microphone, sound processing, AI sound pattern training & recognition, 
Commandline parsing, commandline progress visualization, logging, write files to disk.

**Team setup:** 2 to 3 students.

### 2. Story
>What has happened this night should not be a secret?  

**Me:** *Good sleeping well is the key to beauty and a long life. Can you help me?*   

**You:** *No problem, I'm a Python hero!*


### 3. Functional Requirements / Expected Results
Create a command line tool, named **snoringtracker.py** that... 

1. ...starts to capture and log snoring noise until it is stopped beauty
   the user by a keypress. 


2. ...after it was stopped, it creates a nice visual summary and evaluation
   about what happened in the last night, e.g. some nice charts, a textual 
   summary and (funny) rating of the night. This should be a HTML web page. 


3. ...saves all snoring noise to the folder "/recordings/..." as mp3 files. 
   Snoring mp3's should have the following file name format:
   - /recordings/**[date yyyymmdd]-[start-time hhmmss]-[end-time hhmmss].mp3**
    
   Example:
   - /recordings/**20210501-011500-011843.mp3**
    

4. ...can take a pickle with a custom trained AI model for snorkling sound data
   recognition. Samples:
   - **snoringtracker.py "models/my_snoring_model.pkl"**
   

5. ...supports for a help function to advice users on tool usage by entering 
   **'snoringtracker.py /help'** or ** 'snoringtracker.py /h'** on Windows or respective
   **'snoringtracker.py --help'** or  ** 'snoringtracker.py --h'** on Mac/Unix.


### 4. Success Criteria
A GitHub repository (public or private) that everyone can clone/download and that
directly starts up after the requirements listed in ***requirements.txt*** are fulfilled.

### 5. To get you started...
 - Start here: https://www.kdnuggets.com/2020/02/audio-data-analysis-deep-learning-python-part-1.html
 - PLaying an recording sound: https://realpython.com/playing-and-recording-sound-python/
 - Python library: https://github.com/tyiannak/pyAudioAnalysis
 - A Deep Learning Model for Snoring Detection and Vibration Notification Using a 
   Smart Wearable Gadget https://www.mdpi.com/2079-9292/8/9/987/pdf