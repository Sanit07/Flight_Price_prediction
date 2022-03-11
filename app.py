from fileinput import filename
from flask import Flask,request,render_template
import pickle
import pandas as pd
import sklearn,os

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods= ["POST"])
def predict():
    if request.method == "POST":
        Total_Stops = int(request.form["stops"])

        Dep_Time = request.form["Dep_Time"]
        day_of_journey = int(pd.to_datetime(Dep_Time,format="%Y-%m-%dT%H:%M").day)
        month_of_journey = int(pd.to_datetime(Dep_Time,format="%Y-%m-%dT%H:%M").month)
        dep_hour = int(pd.to_datetime(Dep_Time,format="%Y-%m-%dT%H:%M").hour)
        dep_min = int(pd.to_datetime(Dep_Time,format="%Y-%m-%dT%H:%M").minute)

        Arrival_Time = request.form["Arrival_Time"]
        Arrival_Time_hour = int(pd.to_datetime(Arrival_Time,format="%Y-%m-%dT%H:%M").hour)
        Arrival_Time_minutes = int(pd.to_datetime(Arrival_Time,format="%Y-%m-%dT%H:%M").minute)

        Duration_hours = abs(Arrival_Time_hour - dep_hour)
        Duration_mins = abs(Arrival_Time_minutes - dep_min)

        airline = request.form["airline"]

        
        if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
            
        elif (airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        source = request.form["Source"]
        if source == "Chennai":
            Chennai = 1
            Delhi_s = 0
            Kolkata_s = 0
            Mumbai = 0
        elif source == "Delhi":
            Chennai = 0
            Delhi_s = 1
            Kolkata_s = 0
            Mumbai = 0
        elif source == "Kolkata":
            Chennai = 0
            Delhi_s = 0
            Kolkata_s = 1
            Mumbai = 0
        elif source == "Mumbai":
            Chennai = 0
            Delhi_s = 0
            Kolkata_s = 0
            Mumbai = 1

        Destination = request.form['Destination']
        if Destination == "Cochin":
            Cochin = 1
            Delhi_d = 0
            Hyderabad = 0
            Kolkata_d = 0
            New_Delhi = 0
        elif Destination == "Delhi":
            Cochin = 0
            Delhi_d = 1
            Hyderabad = 0
            Kolkata_d = 0
            New_Delhi = 0
        elif Destination == "New Delhi":
            Cochin = 0
            Delhi_d = 0
            Hyderabad = 0
            Kolkata_d = 0
            New_Delhi = 1

        elif Destination == "Hyderabad":
            Cochin = 0
            Delhi_d = 0
            Hyderabad = 1
            Kolkata_d = 0
            New_Delhi = 0
        elif Destination == "Kolkata":
            Cochin = 0
            Delhi_d = 0
            Hyderabad = 0
            Kolkata_d = 1
            New_Delhi = 0
       
        columns = ['Total_Stops', 'day_of_journey', 'month_of_journey', 'dep_hour',
       'dep_min', 'Arrival_Time_hour', 'Arrival_Time_minutes',
       'Duration_hours', 'Duration_mins', 'Air India', 'GoAir', 'IndiGo',
       'Jet Airways', 'Jet Airways Business', 'Multiple carriers',
       'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara',
       'Vistara Premium economy', 'Chennai', 'Delhi_s', 'Kolkata_s', 'Mumbai',
       'Cochin', 'Delhi_d', 'Hyderabad', 'Kolkata_d', 'New_Delhi']


        prediction = model.predict(pd.DataFrame([[Total_Stops, day_of_journey, month_of_journey, dep_hour,
        dep_min, Arrival_Time_hour, Arrival_Time_minutes,
        Duration_hours, Duration_mins, Air_India, GoAir, IndiGo,
        Jet_Airways, Jet_Airways_Business, Multiple_carriers,
        Multiple_carriers_Premium_economy, SpiceJet, Trujet, Vistara,
        Vistara_Premium_economy, Chennai, Delhi_s, Kolkata_s, Mumbai,
        Cochin, Delhi_d, Hyderabad, Kolkata_d, New_Delhi]],columns=columns))

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))
    return render_template("home.html")    

            
if __name__ == "__main__":
    app.run(debug=True)

