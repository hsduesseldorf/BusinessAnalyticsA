### Business Analytics A - Use Case
**[...back to use case list](/../../blob/main/README.md)**

# 008 - Time Series Forecasting
### 1. Use Case Classification
**Complexity:**  low to medium complex use case with focus on 
time series forecasting and web visualization. 

**Challenges:** time series procession and prediction, web gui programming,
data visualization.

**Team setup:** 2 to 3 students.

### 1. Purpose
> "Tell me about the future."

**Me:** *Can you predict from my sales figures in Excel?*   

**You:** *No problem, I'm a Python hero!*


### 2. Functional Requirements / Expected Results
Create a command line tool, named **tspredict.py** that... 

1. ...spins up a web server and nice helpful web page where users can easily 
   predict time series from files they can upload (csv, txt, xls, xlsx etc.).


2. ...The uploaded file needs to be analysed and processed automatically.
  - understand the format and structure of the file (e.g. are headers defined)
  - detect column types and contents (e.g. date field, value fields, attribute 
    fields)
  - detect what should be forecasted and for how far into the future the forecast
    would be meaningful.
    

3. ...Generate a nice HTML output: e.g. chart with timeseries, predictions, confidence 
   intervals, tabular view etc.
   
  
4. ...supports for a help function to advice users on tool usage by entering 
   **'tspredict.py /help'** or ** 'tspredict.py /h'** on Windows or respective
   **'tspredict.py --help'** or  ** 'tspredict.py --h'** on Mac/Unix.


### 3. Success Criteria
A GitHub repository (public or private) that everyone can clone/download and that
directly starts up after the requirements listed in ***requirements.txt*** are fulfilled.

### 4. To get you started...
 - Start here: *Timeseries Forecasting with Prophet in Python*
   https://machinelearningmastery.com/time-series-forecasting-with-prophet-in-python
 - Time Series Visualization: https://towardsdatascience.com/an-end-to-end-project-on-time-series-analysis-and-forecasting-with-python-4835e6bf050b
 - Sample datasets: https://machinelearningmastery.com/time-series-datasets-for-machine-learning/
 

