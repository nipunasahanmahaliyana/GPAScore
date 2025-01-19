from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io
import matplotlib.ticker as ticker

plt.switch_backend('Agg')

application = Flask(__name__)

gpa_score=pd.read_csv('data.csv')

model=pickle.load(open('model.pkl','rb'))

@application.route('/login')
def login():
    return render_template("login.html")

@application.route('/register')
def register():
    return render_template('account.html')

@application.route('/')
def home():
    return render_template("index.html")

@application.route('/home/dashboard')
def dashboard():
    return render_template("dashboard.html")

@application.route('/home/dashboard/factors')
def fact():
    x=[1,2,3,4]
    y=[0,0,0,0]
    z=0
    for i in x:
        val = gpa_score[gpa_score['The academic year you study ( ex.1 year, 2 year )']==i]
        val_count = gpa_score[gpa_score['The academic year you study ( ex.1 year, 2 year )']==i].shape[0]
        print(val_count)
        count_gpa=val[val['Xaxis']==1].shape[0]
        print(count_gpa)

        prob = (count_gpa/val_count)
        y[z]=prob
        z=z+1

        x=['First year','Second year','Third year','Fourth year']
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
        plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
        plt.ylabel('Probability for GPA 3.00+')
        plt.xlabel('Academic year')
        plt.ylim(0,1)
        for value in y:
                plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
        plt.grid()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data = base64.b64encode(buffer.read()).decode('utf-8')
        plt.close()
        

    male_df = gpa_score[gpa_score['Gender'] == 1]
    male_sum = male_df['Xaxis'].sum()
    print(male_sum)

    sum = gpa_score[gpa_score['Gender'] == 1].shape[0]
    x_sum=male_sum/sum;
    print(male_sum/sum)

    female_df = gpa_score[gpa_score['Gender'] == 0]
    female_sum = female_df['Xaxis'].sum()

    fe_sum = gpa_score[gpa_score['Gender'] == 0].shape[0]

    y_sum=female_sum/fe_sum
    print(female_sum/fe_sum)

    x =[x_sum,y_sum]
    y=['Male','Female']
    plt.xlabel('Gender')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in x:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.plot(y,x , marker='o',markerfacecolor='blue', markersize=8)
    plt.grid()
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data2 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    x=[22,23,24,25,26,27,28]
    y=[0,0,0,0,0,0,0]
    z=0
    for i in x:
        val =gpa_score[gpa_score['Age ']==i]
        val_count = gpa_score[gpa_score['Age ']==i].shape[0]

        count_gpa = val[val['Xaxis']==1].shape[0]
        
        if(val_count==0):
            prob=0
        else:
            prob = count_gpa/val_count

        y[z]=prob
        z=z+1
    
    plt.ylabel('Probability for GPA 3.00+')
    plt.xlabel('Age')
    plt.plot(x,y,marker='o',markerfacecolor="blue",markersize=12)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    plt.ylim(0,1)
    for value in y:
            plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data3 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    x=["Weak ","Below average","Average" ,"Above average","Strong","Very strong"]
    y = [0,1,2,3,4,5]

    y=[0,1,2,3,4,5]
    for i in y:
        value = gpa_score[gpa_score['Are you Physically and Mentally strong ?']==i]
        value_count= gpa_score[gpa_score['Are you Physically and Mentally strong ?']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        if value_count==0:
              y[i]==0
        else:
            y[i]=gpa/value_count

    print(y)
    
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Strongability')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in y:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data4 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    arr=[0,3,5]
    for i in range(len(arr)):
        value = gpa_score[gpa_score['Are you suffering from personal circumstances (personal problems)  ?']==arr[i]]
        value_count= gpa_score[gpa_score['Are you suffering from personal circumstances (personal problems)  ?']==arr[i]].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        x=gpa/value_count
        arr[i]=x
        
    x=arr
    y=["No, not at all" ," Sometimes" ," Yes, constantly"]
    plt.plot(y,x,marker='o', markerfacecolor='blue', markersize=12)
    plt.grid()
    for value in x:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05)) 
    plt.ylabel('Probability for GPA 3.00+')
    plt.xlabel('Suffering Personal Circumantances')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data5 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    arr=['Yes','No']
    value = gpa_score[gpa_score['Do you have currently any long-term or chronic diseases?']==1]
    value_count= gpa_score[gpa_score['Do you have currently any long-term or chronic diseases?']==1].shape[0]
    gpa = value[value['Xaxis']==1].shape[0]
    x_=gpa/value_count

    value = gpa_score[gpa_score['Do you have currently any long-term or chronic diseases?']==0]
    value_count= gpa_score[gpa_score['Do you have currently any long-term or chronic diseases?']==0].shape[0]
    gpa = value[value['Xaxis']==1].shape[0]
    x__=gpa/value_count

    x=[x_,x__]
    y=arr

    plt.plot(y,x,marker='o', markerfacecolor='blue', markersize=12)
    for value in x:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05)) 
    plt.ylabel('Probability- GPA>=3.0')
    plt.xlabel('Having a diseas')
   
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data6 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    y=["No", "Daily" ,"Weekly","Monthly"]
    x=[0,1,2,3]
    for i in x:
        value = gpa_score[gpa_score['Do you consume alcoholic beverages and/or smoke tobacco products? If yes, please specify the day']==i]
        value_count= gpa_score[gpa_score['Do you consume alcoholic beverages and/or smoke tobacco products? If yes, please specify the day']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        if value_count==0:
              x[i]==0
        else:
            x[i]=gpa/value_count
       
    print(x)
    plt.figure(figsize=(8, 6)) 
    plt.plot(y,x,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Alocohol usage')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in x:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data7 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    y=["Poor", "Needs \n improvement" ,"Fair"," Good","Very good","Excellent"]
    x=[0,1,2,3,4,5]
    for i in x:
        value = gpa_score[gpa_score['How about your Study Habits?']==i]
        value_count= gpa_score[gpa_score['How about your Study Habits?']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        x[i]=gpa/value_count

    print(x)
    plt.figure(figsize=(8, 6)) 
    plt.plot(y,x,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Study habits')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in x:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data8 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    y=["Poor", "Needs \n Improvement" ,"Fair","Good","Very \n Good","Excellent"]
    x=[0,1,2,3,4,5]
    for i in x:
        value = gpa_score[gpa_score['How is your Time management skills?']==i]
        value_count= gpa_score[gpa_score['How is your Time management skills?']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        if value_count==0:
              x[i]==0
        else:
            x[i]=gpa/value_count
       
    print(x)
    plt.figure(figsize=(8, 6)) 
    plt.plot(y,x,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Time Management')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in x:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data9 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()


    x=["No, rarely ","Occasionally " ,"Sometimes ", " Often  ", "Regularly ","Yes, always "]
    y=[0,1,2,3,4,5]
    for i in y:
        value = gpa_score[gpa_score['Do you regularly attend the classes ?']==i]
        value_count= gpa_score[gpa_score['Do you regularly attend the classes ?']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        if value_count==0:
              y[i]==0
        else:
            y[i]=gpa/value_count

    print(y)
    
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Regular attendence')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in y:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data10 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    x=["Not at all","Minimal","Moderate","Average","Active","Very active"]
    y=[0,1,2,3,4,5]
    for i in y:
        value = gpa_score[gpa_score['Do you actively participate in classes ?']==i]
        value_count= gpa_score[gpa_score['Do you actively participate in classes ?']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        if value_count==0:
              y[i]==0
        else:
            y[i]=gpa/value_count

    print(y)
    
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Active participation')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in y:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data11 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    x=["Poor"," Needs \n improvement ","Fair ","Good","Very good","Excellent "]
    y=[0,1,2,3,4,5]
    for i in y:
        value = gpa_score[gpa_score['How about your preparation for Exams and Assignments?']==i]
        value_count= gpa_score[gpa_score['How about your preparation for Exams and Assignments?']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        if value_count==0:
              y[i]==0
        else:
            y[i]=gpa/value_count

    print(y)
    plt.figure(figsize=(8, 6)) 
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Preparation')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in y:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data12 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    x=["Minimal","Limited","Some","Moderate","High","Very high"]
    y=[0,1,2,3,4,5]
    for i in y:
        value = gpa_score[gpa_score['What about your engagement with course materials?']==i]
        value_count= gpa_score[gpa_score['What about your engagement with course materials?']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        if value_count==0:
              y[i]==0
        else:
            y[i]=gpa/value_count

    print(y)
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Engagement with course materials')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in y:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data13 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    x=["Weak","Limited","Adequate","Good","Strong ","Excellent"]
    y=[0,1,2,3,4,5]
    for i in y:
        value = gpa_score[gpa_score['How strong your academic support systems?']==i]
        value_count= gpa_score[gpa_score['How strong your academic support systems?']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        if value_count==0:
              y[i]==0
        else:
            y[i]=gpa/value_count

    print(y)
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Support Systems')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in y:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data14 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    x=["No, not at all","Rarely","Occasionally","Sometimes","Often","Yes, always"]
    y=[0,1,2,3,4,5]
    for i in y:
        value = gpa_score[gpa_score['Do you set an academic goals yourself and motivate yourself to achieve them?']==i]
        value_count= gpa_score[gpa_score['Do you set an academic goals yourself and motivate yourself to achieve them?']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        if value_count==0:
              y[i]==0
        else:
            y[i]=gpa/value_count

    print(y)
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Academic goals')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in y:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data15 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    
    x=["Poor","Below average","Average","Above average","Good","Excellent"]
    y=[0,1,2,3,4,5]
    for i in y:
        value = gpa_score[gpa_score['How about your faculty and the instructions they(lectures) give?']==i]
        value_count= gpa_score[gpa_score['How about your faculty and the instructions they(lectures) give?']==i].shape[0]
        gpa = value[value['Xaxis']==1].shape[0]
        if value_count==0:
              y[i]==0
        else:
            y[i]=gpa/value_count

    print(y)
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Faculty and the instructions')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in y:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()
    plt.show()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data16 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    x=["No, not at all "," Unsatisfied","Somewhat \n unsatisfied ","Neutral","Satisfied","Very satisfied"]
    y=[0,1,2,3,4,5]
    for i in y:
            value = gpa_score[gpa_score['Do you satisfy with your learning environment?']==i]
            value_count= gpa_score[gpa_score['Do you satisfy with your learning environment?']==i].shape[0]
            gpa = value[value['Xaxis']==1].shape[0]
            if value_count==0:
                y[i]==0
            else:
                y[i]=gpa/value_count

    print(y)
    plt.figure(figsize=(8, 6)) 
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Learning environment')   
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in y:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data17= base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    
    x=["I can't","Not sure ","Maybe","Likely","Probably","Definitely"]
    y=[0,1,2,3,4,5]
    for i in y:
            value = gpa_score[gpa_score['Can you able to  understand the things you study?']==i]
            value_count= gpa_score[gpa_score['Can you able to  understand the things you study?']==i].shape[0]
            gpa = value[value['Xaxis']==1].shape[0]
            if value_count==0:
                y[i]==0
            else:
                y[i]=gpa/value_count

    print(y)
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Understanbility')
    plt.ylabel('Probability for GPA 3.00+')
    plt.ylim(0,1)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    for value in y:
        plt.axhline(y=value, color='r', linestyle='--', linewidth=1)
    plt.grid()
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data18= base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return render_template("factorsta.html", plot_data=plot_data,plot_data2=plot_data2,plot_data3=plot_data3,plot_data4=plot_data4,plot_data5=plot_data5,plot_data6=plot_data6,plot_data7=plot_data7,plot_data8=plot_data8,plot_data9=plot_data9,plot_data10=plot_data10,plot_data11=plot_data11,plot_data12=plot_data12,plot_data13=plot_data13,plot_data14=plot_data14,plot_data15=plot_data15,plot_data16=plot_data16,plot_data17=plot_data17,plot_data18=plot_data18)


@application.route('/home/dashboard/features')
def factors():
    return render_template("factor.html")

@application.route('/home/dashboard/predict')
def predict():
    return render_template("predict.html")

@application.route('/home/dashboard/predict/rate')
def rate():
    return render_template("rate.html")

@application.route('/home/dashboard/logout')
def logout():
    return render_template('logout.html')

@application.route('/home/dashboard/predict/rate/collect',methods=['POST','GET'])
def collect():
    try:
        int_features=[int(x) for x in request.form.values()]
        print(int_features)

        x=int_features
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
        
        if(pred[0]==0):
            return render_template("finalGpa.html",message = "3.00 -")
        else:
            return render_template("finalGpa.html",message = "3.00 +")
     
    except Exception  as e:
        return render_template("finalGpa.html",message="Error occured,Answre the all questions...")

if __name__ == '__main__':
    application.run(debug=True)
    