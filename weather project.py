import requests
from pprint import pprint
import tkinter
from tkinter import *
import datetime
from datetime import date


root=tkinter.Tk()
root.geometry("350x90")
root.title("Sunshine")
img = PhotoImage(file='weather.png')
root.tk.call('wm', 'iconphoto', root._w, img)
mycolor = '#%02x%02x%02x' % (64, 204, 208)  # set your favourite rgb color
mycolor2 = '#40E0D0'  # or use hex if you prefer 
root.configure(bg=mycolor)
tkinter.Button(root, text="Press me!", bg=mycolor, fg='white',
               activebackground='red', activeforeground=mycolor2).grid()

root.resizable(False,False)
def show():
    root.geometry("350x500")
    x=(entry_city.get())
    print(x)
    url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=d1a7ed688e1b9155f95106d9a55b9ab0&units=metric'.format(x)
    res=requests.get(url)
    data=res.json()
    temp=str(data['main']['temp'])+' degree celcius'
    wind_speed=str(data['wind']['speed'])+' m/s'
    latitude=data['coord']['lat']
    longitude=data['coord']['lon']
    description=data['weather'][0]['description']
    pressure=str(data['main']['pressure'])+' hPa'
    temp_max=str(data['main']['temp_max'])+' degree celsius'
    temp_min=str(data['main']['temp_max'])+' degree celsius'
    humidity=str(data['main']['humidity'])+' %'
    country=data['sys']['country']
    wind_direction=str(data['wind']['deg'])+' degree'
    pprint(data)
    print('Temperature:{} '.format(temp))
    print('wind speed:{}'.format(wind_speed))
    print('Latitude:{}'.format(latitude))
    print('Longitude:{}'.format(longitude))
    print('Description:{}'.format(description))
    print('Pressure:{}'.format(pressure))
    print('Temperature max:{} '.format(temp_max))
    print('Temperature min:{} '.format(temp_min))
    print('Humidity:{}'.format(humidity))
    print('Country:{}'.format(country))
    print('Wind Direction:{}'.format(wind_direction))

    current_date = datetime.date.today()
    print(current_date)


    date.config(text=current_date)
    city.config(text=x)
    l.config(text=temp)
    l1.config(text=wind_speed)
    l2.config(text=latitude)
    l3.config(text=longitude)
    l4.config(text=description)
    l5.config(text=pressure)
    l6.config(text=temp_max)
    l7.config(text=temp_min)
    l8.config(text=humidity)
    l9.config(text=country)
    l10.config(text=wind_direction)



label_city=Label(root,text="City",width=6,font=90,bg='pink')
label_city.grid(row=0,column=0,pady=6)
entry_city=Entry(root,width=30)
entry_city.grid(row=0,column=1)
b=Button(root,text="Show Weather",width=15,bg='red',fg='black',command=show)
b.grid(row=1,column=1)
city=Label(root,text="",font=30,bg='#%02x%02x%02x' % (64, 204, 208))
city.grid(row=2,column=1,pady=4)
date=Label(root,text="",font=30,bg='#%02x%02x%02x' % (64, 204, 208))
date.grid(row=3,column=1,pady=4)
temp=Label(root,text="Temperature  :-",font=15,bg='green')
temp.grid(row=4,column=0)
l=Label(root,text="",bg='green')
l.grid(row=4,column=1)
wind=Label(root,text="Wind Speed  :-",font=15,bg='green')
wind.grid(row=5,column=0)
l1=Label(root,text="",bg='green')
l1.grid(row=5,column=1)
latitude=Label(root,text="Latitude  :-",font=15,bg='green')
latitude.grid(row=6,column=0)
l2=Label(root,text="",bg='green')
l2.grid(row=6,column=1)
longitude=Label(root,text="Longitude  :-",font=15,bg='green')
longitude.grid(row=7,column=0)
l3=Label(root,text="",bg='green')
l3.grid(row=7,column=1)
description=Label(root,text="Description  :-",font=15,bg='green')
description.grid(row=8,column=0)
l4=Label(root,text="",bg='green')
l4.grid(row=8,column=1)
pressure=Label(root,text="Pressure :-",font=15,bg='green')
pressure.grid(row=9,column=0)
l5=Label(root,text="",bg='green')
l5.grid(row=9,column=1)
temp_max=Label(root,text="Temperature Max :-",font=15,bg='green')
temp_max.grid(row=10,column=0)
l6=Label(root,text="",bg='green')
l6.grid(row=10,column=1)
temp_min=Label(root,text="Temperature Min :-",font=15,bg='green')
temp_min.grid(row=11,column=0)
l7=Label(root,text="",bg='green')
l7.grid(row=11,column=1)
humidity=Label(root,text="Humidity :-",font=15,bg='green')
humidity.grid(row=12,column=0)
l8=Label(root,text="",bg='green')
l8.grid(row=12,column=1)
country=Label(root,text="Country :-",font=15,bg='green')
country.grid(row=13,column=0)
l9=Label(root,text="",bg='green')
l9.grid(row=13,column=1)
wind_direction=Label(root,text="Wind Direction :-",font=15,bg='green')
wind_direction.grid(row=14,column=0)
l10=Label(root,text="",bg='green')
l10.grid(row=14,column=1)


root.mainloop()
