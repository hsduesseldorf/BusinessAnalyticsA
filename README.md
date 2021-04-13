*...this repository belongs to lectures **Business Analytics A** of master studies in 
[Business Analytics](https://wiwi.hs-duesseldorf.de/en/student-affairs/study-programmes/master-business-analytics)
at faculty of [Business Studies](https://wiwi.hs-duesseldorf.de/en)
from [HSD University of Applied Science](https://hs-duesseldorf.de/en) (Düsseldorf, Germany)
by [Thomas Zeutschler](https://wiwi.hs-duesseldorf.de/personen/thomas.zeutschler/Seiten/default.aspx)*

![HSD logo](/images/HSD_logo.png)

# Business Analytics A - *Use Cases Summer 2021*  
Working on Use Cases in Git Hub is intended to be a fully-digitized replacement 
of a student term papers. Instead of a written paper, students have to create 
and work in a single code repository on GitHub. In this directory the use case 
is entirely processed, implemented and documented. 

Use cases are most often designed to be each processed by a team 2 to 3 (or more) 
students. Reasons: As a team you don't get stuck so easily, you can distribute 
the workload on more shoulders, you need to coordinate the team and especially 
because ***teamwork is simply more fun***. 

### Assignment of use cases to teams
Each individual use case will be processed by one single team. Teams will be put 
together randomly from all registered students by a Python program. Use cases will
then be assigned randomly to the available teams.

Here's a simple Python script to randomly assign students to the use cases:
[students_to_case.py](/code/students_to_case.py) 

### Use cases objectives
The use cases have been designed to reflect the contents, focus topics and 
learning objectives of the **Business Analytics A** class with the 
**M.Sc. Business Analytics** studies at **HSD University of Applied Science, 
Düsseldorf**. These are:
- Introduction to Professional Programming with Python
- Agile Software Project Management and Application Lifecycle Management using GitHub
- Development of Analytical Solutions
- Collaboration in asynchronous teams with distributed responsibilities.


# A. Available use cases
Teams are allowed and encouraged to propose additional use cases. But only 
before the use cases get randomly assigned to the individual teams. Hence,
there is no right to get assigned to a certain use case. All is based on luck.

### 001 - Earth Quake Detector
Realtime detection and visualization of earth quake
occurrences in predefined region (map segment) over a certain time.

**[001-earthquake-detector](/cases/001-earthquake-detector/README.md)**

### 002 - Audio News Podcast Generator
Automated generation of a podcast from relevant news available on the internet.

**[002-audio-news-podcast-generator](/cases/002-audio-news-potcast-generator/README.md)**

### 003 - Plane Close Crash Detector
Realtime visualization and detection of "close to crash approximations"
of airplanes in a defined area/region.

**[003-plane-close-crash-detector](/cases/003-plane-close-crash-detector/README.md)**

### 004 - Twitter Sentiment Analyzer
Analyze the sentiment of reactions on a single Twitter tweet and how they develop 
and change over time.

**[004-twitter-sentiment-analyzer](/cases/004-twitter-sentiment-analyzer/README.md)**

### 005 - Twitter Weighted Follower Analyzer
Stunning visualization of followers on Twitter.

**[005-twitter-weighted follower-graph](/cases/005-twitter-weighted-follower-graph/README.md)**

### 006 - Employee Attrition Analysis
Implement a web service to analyse employee data to identify employees 
likely to leave the company to be able to initiate counter measures.

**[006-employee-attrition-analysis](/cases/006-employee-attrition-analysis/README.md)**

### 007 - Parquet File Viewer
Implement a web service to display and analyze files in
the popular Parquet data file format.

**[007-parquet-file-viewer](/cases/007-parquet-file-viewer/README.md)**


### 008 - Time Series Forecasting
Implement a web service to forecast any file containing time series data
with just one click.

**[008-timeseries-forecasting](/cases/008-timeseries-forecasting/README.md)**


### 009 - Personal Alexa-like Speech Service
Implement an Alexa alike speech service in Python.

**[009-personal-alexa-like-speech-service](/cases/009-personal-alexa-like-speech-service/README.md)**


### 010 - Night Time Noise and Snoring Tracker and Recorder
Implement a sleeping and snoring tracker in Python
that monitors, analyses and logs any relevant noise over the night.

**[010-nighttime-noise-and-snoring-tracker](/cases/010-nighttime-noise-and-snoring-tracker/README.md)**


# B. How to process use cases
In order to meet the examination requirements of the HSD University of Applied 
Sciences (Düsseldorf), the following structure, procedures and standards must be followed.
They are the basis for the grading of your use case. If you miss them you may get 
downgraded by up to 2. grades. e.g.: you achieved a perfect result for your use case 
= 1.0, maybe even worth the next Nobel-Prize, but you totally missed the requirements 
in regard of size and code quality and structure, then you might get downgraded up 
to 4.0. *So, better be careful in following these rules...*


### 1. The use of a dedicated GitHub repositories
Backbone of each use case is a dedicated (not a shared) GitHub repository. Anything
within this repository counts for evaluation, anything outside does not.

The repository can be private (recommended) or public and needs to be created by one
of the team members. If the repository is private, then the team has to ensure that
- all **students of the team** have **read/write** access to the repository.
- the **teacher** has **read/write** access (just in case you need support).
- **all other students** of the current class have **read** access only.

If the repository is public, then the team has to ensure that
- all **students of the team** have **read/write** access to the repository.
- the **teacher** has **read/write** access (just in case you need support).

***WARNING***: A repository with granted access as described above will **be rated
as non-existing**. So better handle and check access right with care. 

### 2. The README.md file
The file **README.md** represents the central entry point and your main contributions
for the evaluation and examination of the given use case. This document needs to contain
at least 10.000 characters, but not more than 100.000 characters. 

**Important:** The number of characters in will be evaluated by automated processes and, 
if outside this range, will reduce the grading of the use case evaluation by 0,5 grades 
(from 1.0 best down to 6.0 worst). *Hence, better count your characters...*

For advice on how to write and format MarkDown files please visit (either or both):
 - https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
 - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

The **README.md** file must be written **in English language** (expections on request only)
and has to contain the following mandatory information in the following order:

 1. **At the very top of the file**, a list of first name and last name followed 
    by the matriculation number in squared brackets '[...]' for all students 
    involved in and to be evaluated for the given use case. Other contributors 
    must be listed without brackets and marticulation number. *Sample:* The 
    following markdown code would create a valid output. Only Peter Parker and 
    Precilla Presley will evaluted for the use case.
    ```
    - Peter Peter [7436450]
    - Precilla Presley [7442803]
    - Bob the Bausmeister (supporting on GitHub Actions)
    - Sharon Zurkoswsky
    ```
    
 2. The title of the use case, exactly as defined by the lecturer (letter by letter)
    formatted as top level headline.Sample for valid markdown:
    ```
    # B2B Customer Churn Analysis
    ```
    
 3. Any subsequent text, images,tables, links, code fragments and anything else 
    that explains/contains:
    
    1. What was the task to be accomplished? What was intended to achieve?
       *Sometime analytics projects fail or end up with the insight that the user
       problem can not be solved. This is also a valid and valuable result.*
       
    2. Description and your understanding of the business question or problem, 
       analytical question and/or technical problem associated with the use case.
       
    3. The methodological approach chosen to process and implement the use case.   
       For analytical uses cases it is wise to follow a structured approach like
       Microsoft's [Team Database Science Process](https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/overview),
       which is the legitimate successor of the CrispDM methodology.
       
    4. **Most important**: A detailed description of your approach, work, findings 
       and concrete achievements towards the use case. Here you should accumulate 
       the largest part of your writing.
       
    5. A summary if the targets have been achieved, and if not - and whatever the 
       reason is - why it wasn't achieved.


### 3. Proper Source Code
Any source code, may it be written in Python or any other programming language, 
will be automatically validated and evaluated against common coding standards 
and best practises. If the measured formal code quality drops below a certain threshold,
the grading of the use case evaluation by 0,5 grades up to 1,5 grades (a rare case). 
*Hence, better check your code quality...*

Code quality will be checked against the official ***PEP 8 Style Guide for Python Code***
available at https://www.python.org/dev/peps/pep-0008/. Most important are:
 - All naming conventions
 - Expressive naming of variables, classes and functions (manually by teacher)
 - Proper code indentation
 - Proper source code documentation (classes, functions).
 - Use of empty lines to separate code blocks
 - *and others...*

You can ensure and check proper code quality by a combination of the following methods:

 - While coding, follow the rules defined in the official ***PEP 8 Style Guide for Python Code***.
     
 - Using PyCharm or another professional IDE for coding. They provide real-time code 
   quality evaluation. More details and an introduction to the topic are available here: 
   https://www.jetbrains.com/help/pycharm/tutorial-code-quality-assistance-tips-and-tricks.html
   
 - Checking your code quality manually using dedicated tools, e.g.: 
   - https://pycodestyle.pycqa.org/
   - https://flake8.pycqa.org/en/latest/
   - https://www.jetbrains.com/help/pycharm/command-line-code-inspector.html
   - or simply http://pep8online.com/ 

 - (Recommended) Checking your code quality automatically using a GitHub Action.
   A good intro is given here:
   http://www.grantmcconnaughey.com/blog/2020/02/25/automate-python-code-quality/


### 4. Proper organization of files
Create separate folders for the various artefacts of your use case. If you deal with
data then there should be a separate ```data/...``` folder in your repository. 
If you need to include images in your markdown file(s) then please create separate
put them into a folder ```/docs...```. The folder docs should also contain any
additional documentation for your use case. 

If your repository contains many (Python) code files or even contains a somehow
complex class hierarchy, then it is also wise to structure it via folders.
Follow this approach and your safe: https://github.com/kriasoft/Folder-Structure-Conventions.


### 5. Clever utilization of the Python eco-system
>For every problem on this planet, be sure, there exists at least one 
> Python package that already solves it.

If you are aware of this phenomenon, and also know how to google for Python packages 
and Python solutions (e.g.: [*your question/problem in short words*] followed by the 
phrase *"... in Python"* or *"... Python package"*) and where to get good and 
free community advice for Python coding (https://stackoverflow.com), your use 
case implementaion will become much faster and also more fun.   


### 6. The use of GitHub's project management capabilities
Use GitHub issues to keep track of all the tasks, enhancements and bugs in your 
use case. For more information of issues and how to create them, please review:

 - https://docs.github.com/en/github/managing-your-work-on-github/about-issues
 - https://guides.github.com/features/issues/

Create and use a project to structure and organize your work and tasks. If unsure,
please use the **Basic kanban** template to get started.
For more information please refer to:
 - https://docs.github.com/en/github/managing-your-work-on-github/about-project-boards
 - https://www.youtube.com/watch?v=nI5VdsVl0FM
 - https://www.youtube.com/watch?v=ff5cBkPg-bQ

**Important:** Usage of GitHubs project management capabilities will be automatically evaluated, 
meaning if and to what extend you use GitHub issues and at least GitHub projects. 
If GitHub issues are not, rarely or wrongly use, you might get downgraded by 0,5 grades. If no GitHub project is used
or the project is empty or poorly used, you might get downgraded by another 0,5 grades.
In total, you might loose up to 1,0 grade if you ignore GitHub issues and projects. 
![GitHub Project](/images/ghproject.jpg)



All the best for your use case... 

*Your teacher*





 
