https://realpython.com/python-speech-recognition/
https://spacy.io/
https://stackabuse.com/how-to-send-emails-with-gmail-using-python/


### Business Analytics A - Use Case 
# 009 - Personal Alexa
### 1. Use Case Classification
**Complexity:**  medium complex use case with focus on the statistical 
data analysis and web data visualization. 

**Challenges:** Parquet file format, Pandas, PyArrow, 
Commandline parsing, tabular and chart data visualization.

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


