https://gist.github.com/mabdrabo/8678538
https://www.kdnuggets.com/2020/02/audio-data-analysis-deep-learning-python-part-1.html
https://medium.com/@almeidneto/sound-pattern-recognition-with-python-9aff69edce5d

### Business Analytics A - Use Case 
# 010 - Nightime Noise and Snoring Tracker and Recorder
### 1. Use Case Classification
**Complexity:**  medium complex use case with focus on sensor data  
analysis and real-time data processing. 

**Challenges:** microphone, sound processing, sound pattern recognition, 
Commandline parsing, commandline progress visualization, logging, write files to disk.

**Team setup:** 2 to 3 students.

### 1. Purpose
>Support the data format of the future (Data Scientist's *Liebling*)! 

**Me:** *Can't see what's inside this f *** Parquest file. Please show me!*   

**You:** *No problem, I'm a Python hero!*


### 2. Functional Requirements / Expected Results
Create a command line tool, named **parquetviewer.py** that... 

1. ...comes with a configuration file containing a user-editable list of news 
   sources to be investigated. The primary news source should be public 
   RSS or AtomFeeds, but additional sources are also welcome.
   
   The configuration file should contain a list of at least 30 RSS feeds
   from popular news sources like CNN, NYT, FoxNews, Spiegel an others. 


2. ...takes a list of comma separated keywords or phrases arguments to used 
   to generate and filter the podcast. Some valid samples:
   - **podgen.py Corona**
   - **podgen.py "Angela Merkel"** 
   - **podgen.py "Donald Trump" "Joe Biden"** 
   - **podgen.py --keywords healthy food**
   Multiple search arguments should be combined by an **AND** filter operations.
   

3. ...supports for a help function to advice users on tool usage by entering 
   **'podgen.py /help'** or ** 'podgen.py /h'** on Windows or respective
   **'podgen.py --help'** or  ** 'podgen.py --h'** on MAc/Unix.

     
4. ...displays progress and status information while the podcast is in generation.


5. ...creates an audio file (e.g. MP3), ready for direct consumption.
   Note: The audio file should be created in the current folder.


### 3. Success Criteria
A GitHub repository (public or private) that everyone can clone/download and that
directly works after the requirements listed in ***requirements.txt*** are fulfilled.

### 4. To get you started...
 - Start here: https://github.com/vipinc007/ParquetViewer
 - That's the visual blueprint (see table visualization): https://www.kaggle.com/shubh0799/churn-modelling

![blueprint](viewer.jpg)


