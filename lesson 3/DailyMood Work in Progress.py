import calendar
import datetime

time = datetime.datetime.now()
print("The time is: ", time)

username = input("Type your name (or nickname if you prefer not to use your real name)")
print("Hello ", username)


("What's your mood? 1 = Happy 2 = Tired 3 = Stressed/Anxious 4 = Hungry 5 = Sad 6 = Impatient 7 = Curious ")
mood = input


energy_level = input("On a scale of 1-5, what's your energy level? You can type 20, 40, 60 80, or 100")
if(mood == 1 and energy_level < 50 and energy_level > -1):
    print("It's nice to see you're happy. Your energy level seems low, though. Try getting some rest and eating some food. You might get happier that way!")

elif(mood == 1 and energy_level > 50 and energy_level < 101):
    print("Glad you're happy with a great energy level! Do something nice for yourself, like a fun outing!")

if(mood == 2 and energy_level > 30 and energy_level < 50):
    print("I'm sorry to hear you're tired. Since your energy level is smaller than 30, it's probably best to go take a nap, or if it's bedtime, sleep for the night.")

elif (mood == 2 and energy_level > 79):
    print("Hmm...Try getting some exercise, or eat a little food. Might uplift your mood and energy level.")

else:
    print("We don't typically evaluate energy levels over 100 (or under 0), but if you're happy, please enjoy your day!")
