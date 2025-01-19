import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

data = pd.read_csv('data.csv')

X=data.drop('Xaxis',axis=1)
Y=data['Xaxis']


X_Train,X_Test,Y_Train ,Y_Test= train_test_split(X,Y,test_size=0.2,random_state=42)

model = RandomForestClassifier()
model.fit(X_Train,Y_Train)

pred = model.predict(X_Test)
print(pred)

acc=accuracy_score(Y_Test,pred)
print(acc)

pickle.dump(model,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))



x=[2, 0, 26, 2, 3, 0, 2, 0, 2, 3, 2, 1, 1, 2, 2, 2, 2, 2]
input = pd.DataFrame({
    'The academic year you study ( ex.1 year, 2 year )':[x[0]],
    'Gender':[x[1]],
    'Age ':[x[2]],
    'Are you Physically and Mentally strong ?':[x[3]],
    'Are you suffering from personal circumstances (personal problems)  ?':[x[4]],
    'Do you have currently any long-term or chronic diseases?':[x[5]],
    'Do you consume alcoholic beverages and/or smoke tobacco products? If yes, please specify the day':[x[6]],
    'How about your Study Habits?':[x[7]],
    'How is your Time management skills?':[x[8]],
    'Do you regularly attend the classes ?':[x[9]],
    'Do you actively participate in classes ?':[x[10]],
    'How about your preparation for Exams and Assignments?':[x[11]],
    'What about your engagement with course materials?':[x[12]],
    'How strong your academic support systems?':[x[13]],
    'Do you set an academic goals yourself and motivate yourself to achieve them?':[x[14]],
    'How about your faculty and the instructions they(lectures) give?':[x[15]],
    'Do you satisfy with your learning environment?':[x[16]],
    'Can you able to  understand the things you study?':[x[17]]

    })
    
pred = model.predict(input)
print(pred[0])

