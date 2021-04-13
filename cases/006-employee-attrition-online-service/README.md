https://gist.github.com/mabdrabo/8678538
https://www.kdnuggets.com/2020/02/audio-data-analysis-deep-learning-python-part-1.html
https://medium.com/@almeidneto/sound-pattern-recognition-with-python-9aff69edce5d

### Business Analytics A - Use Case 
# 006 - Employee Attrition Online Service
### 1. Use Case Classification
**Complexity:**  medium complex use case with focus on 
2-class classification and web app development. 

**Challenges:** 2-class classification, auto-feature engineering,
web gui programming, data visualization, flask

**Team setup:** 2 to 3 students.

### 1. Purpose
> "People are the most important asset of a company!"

**Me:** *It's so hard to keep good people in the company. Who might leave?*   

**You:** *No problem, I'm a Python hero!*


### 2. Functional Requirements / Expected Results
Create a command line tool, named **attrition.py** that... 

1. ...spins up a web server and nice helpful web page where users can easily 
   upload a train and test data (csv, txt, xls, xlsx etc.) with employee masterdata 
   to predict attrition. 


2. ...The uploaded file needs to be analysed and processed automatically.
  - understand the format and structure of the file (e.g. are headers defined)
  - detect column types and contents (e.g. date field, value fields, attribute 
    fields)
  - try to detect the attrition (class) field in the train file.
    

3. ...Generate a nice HTML result output: e.g. a table with employees most 
   likely to leave the company sorted by propability, some nice charts etc.
   
  
4. ...supports for a help function to advice users on tool usage by entering 
   **'attrition.py /help'** or ** 'attrition.py /h'** on Windows or respective
   **'attrition.py --help'** or  ** 'attrition.py --h'** on Mac/Unix.


### 3. Success Criteria
A GitHub repository (public or private) that everyone can clone/download and that
directly starts up after the requirements listed in ***requirements.txt*** are fulfilled.

### 4. To get you started...
 - Start here: *[Predict Employee Attrition Using Machine Learning & Python](https://medium.com/analytics-vidhya/predict-employee-attrition-a34e2c5a972d)*
 - Flask: [Uploading files with Flask](https://pythonbasics.org/flask-upload-file/)
 - Sample datasets: [attrition_dataset.xlx](attrition_dataset.xlx)

 

