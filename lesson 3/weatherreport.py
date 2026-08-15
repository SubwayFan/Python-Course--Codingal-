#These lines import calendar and dateimte
import calendar
import datetime
city = input("Give your city ")
temperature = float(input("What is the current temperature?"))

if (temperature > 35):
    print("Warning: It is going to be hot!")
elif (temperature == 35):
    print("I suppose this is a moderate temprature")
elif (temperature > 45):
    print("It can't get any hotter than this! You should stay indoors.")
elif(temperature > 50):
    print("Stay indoors for your own safety just for today.")
elif (temperature < 10):
    print("If you are going to play outside, wear snowpants and a jacket. Maybe take a scarf.")
else:
    print("Moderate temperature.")

if(temperature > 25):
    print("Great weather!")
else:
    print("Grab a jacket!")


#You may attach a variable of any name to datetime.datetime.now(), but the function MUST be written as is
Gabriel = datetime.datetime.now()
print("Time now: ", Gabriel)

print(calendar.calendar(Gabriel.year))