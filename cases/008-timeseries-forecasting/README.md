### Business Analytics A - Use Case
**[...back to use case list](/../../blob/main/README.md)**

# 008 - Time Series Forecasting
**Summary:** Implement a web service to forecast any file containing time series data
with just one click.
### 1. Use Case Classification
**Complexity:**  low to medium complex use case with focus on 
time series forecasting and web visualization. 

**Challenges:** time series procession and prediction, web gui programming,
data visualization.

**Team setup:** 2 to 3 students.

### 2. Story
> "Prediction is very difficult, especially if it's about the future." [Niels Bohr](https://en.wikipedia.org/wiki/Niels_Bohr)

**Me:** *Can you predict my sales figures from this Excel file?*   

**You:** *No problem, I'm a Python hero!*


### 3. Functional Requirements / Expected Results
Create a command line tool, named **tspredict.py** that... 

1. ...spins up a web server and nice and simple to use web page where 
   users can easily predict time series from files they can upload 
   (csv, txt, xls, xlsx etc.).


2. ...the uploaded file needs to be analysed and processed automatically.
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


### 4. Success Criteria
A GitHub repository (public or private) that everyone can clone/download and that
directly starts up after the requirements listed in ***requirements.txt*** are fulfilled.

### 5. To get you started...
 - Start here: *Timeseries Forecasting with Prophet in Python*
   https://machinelearningmastery.com/time-series-forecasting-with-prophet-in-python
 - Time Series Visualization: https://towardsdatascience.com/an-end-to-end-project-on-time-series-analysis-and-forecasting-with-python-4835e6bf050b
 - Sample datasets: https://machinelearningmastery.com/time-series-datasets-for-machine-learning/
 

