#import flsk module
from flask import Flask, render_template, request
import requests #it is a html library that user can use

app = Flask(__name__)

#create a route for all html templates
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        nameOfCity=request.form.get('city')
        
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+nameOfCity+'&appid=e864817336c81747781350f9db05c921')

        json_obj = r.json() #Converting data into json format

        #select data as per our need.
        tempInKelvin = float(json_obj['main']['temp']) # value in kelvin
        humidity = float(json_obj['main']['humidity'])
        windSpeed = float(json_obj['wind']['speed'])
        Description = str(json_obj['weather'][0]['description'])
        tempInCelcius = str(tempInKelvin-273.15) # converting kelvin to celcius

        #transfer data to html template
        return render_template('home.html',nameOfCity=nameOfCity,tempInCelcius=tempInCelcius,humidity=humidity,windSpeed=windSpeed,Description=Description)
    
    else:
        return render_template('home.html') 



if __name__ == '__main__':
    app.run(debug=True)