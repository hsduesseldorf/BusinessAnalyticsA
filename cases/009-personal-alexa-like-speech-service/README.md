https://gist.github.com/mabdrabo/8678538
https://www.kdnuggets.com/2020/02/audio-data-analysis-deep-learning-python-part-1.html
https://medium.com/@almeidneto/sound-pattern-recognition-with-python-9aff69edce5d

### Business Analytics A - Use Case 
# 009 - Personal Alexa-like Speech Service
### 1. Use Case Classification
**Complexity:**  medium complex use case with focus on 
natural language processing. 

**Challenges:** microphone, sound processing, speech-to-text, 
speech assistant.

**Team setup:** 2 to 3 students.

### 1. Purpose
> **HAL 9000**: "I'm sorry Dave, I'm afraid I can't do that."
> https://youtu.be/ARJ8cAGm6JE

**Me:** *HAL, please... Can someone else help me?*   

**You:** *No problem, I'm a Python hero!*


### 2. Functional Requirements / Expected Results
Create a command line tool, named **hal.py** that... 

1. ...starts to listen after "Hello Hal" (or some other vocal trigger).


2. ...takes a sentence spoken by the user (the input ends after 3 sec of silence).


3. ...converts the audio input into written text. 


4. ...processes the text (somehow) and creates a valuable (or just a funny) 
   answer.
   

5. ...the asnwer is given in spoken words. 


6. ...supports for a help function to advice users on tool usage by entering 
   **'hal.py /help'** or ** 'hal.py /h'** on Windows or respective
   **'hal.py --help'** or  ** 'hal.py --h'** on Mac/Unix.


### 3. Success Criteria
A GitHub repository (public or private) that everyone can clone/download and that
directly starts up after the requirements listed in ***requirements.txt*** are fulfilled.

### 4. To get you started...
 - Start here: *The Ultimate Guide To Speech Recognition With Python*
   https://realpython.com/python-speech-recognition/
 - Text processing: https://spacy.io
 - Text-to-Speech: e.g. https://pypi.org/project/pyttsx3/
 
