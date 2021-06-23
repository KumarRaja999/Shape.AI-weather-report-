import requests
#import os
from datetime import datetime
api_key = 'cc87f5071a40b392841d106c36707938'
location = input("Enter the city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")
print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
file1 = open("Weather report.txt","w")#write mode
file1.write("                   Weather\n")
file1.write('current temprature:'+str(temp_city)+'\n')
file1.write('current weather desc :'+str(weather_desc)+' \n')
file1.write('Current Humidity:'+str(hmdt)+'%\n')
file1.write('Current wind speed:'+str(wind_spd)+'kmph\n')
file1.close()
file1 = open("myfile.txt","r")
print ("Output of Readlines after writing")
print ('stay home stay happy')
file1.close()