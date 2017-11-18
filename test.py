weather1 = {'city':'Moscow', 'temperature':20, 'wind':'east', 'date':'27.05.2017'}
weather2 = {'city':'Vologda', 'temperature':13, 'wind':'north', 'date':'27.05.2017'}
weather3 = {'city':'Helsinki', 'temperature':15, 'wind':'north', 'date':'11.11.2016'}

weather_name = {'Paul':weather1, 'Masha':weather2, 'Petri':weather3}

name = input('Enter your name, bro ')

print(weather_name[name])