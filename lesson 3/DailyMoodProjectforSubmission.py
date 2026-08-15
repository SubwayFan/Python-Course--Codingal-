import calendar
import datetime

time = datetime.datetime.now()
print("The time is: ", time)

username = input("Type your name (or nickname if you prefer not to use your real name)")
print("Hello ", username)


mood = input("What's your mood? Type 1 or 2. 1 = Happy 2 = Tired ")



energy_level = 0

energy_level = input("What's your energy level? Type between 1 and 100 ")

print("")

if(mood == 1 and energy_level < 50 and energy_level > -1):
    print("It's nice to see you're happy. Your energy level seems low, though. Try getting some rest and eating some food. You might get happier that way!")

elif(mood == 1 and energy_level > 50 and energy_level < 101):
    print("Glad you're happy with a great energy level! Do something nice for yourself, like a fun outing!")

elif(mood == 2 and energy_level > 30 and energy_level < 50):
    print("I'm sorry to hear you're tired. Since your energy level is smaller than 30, it's probably best to go take a nap, or if it's bedtime, sleep for the night.")

elif (mood == 2 and energy_level > 79 and energy_level < 90):
    print("Hmm...Try getting some exercise, or eat a little food. Might uplift your mood and energy level.")
elif (mood == 2 and energy_level > 89 and energy_level < 101):
    print("You're tired, but your energy level is at 100? Hmm, at the very least I'd get some rest. Perhaps sit around for a few minutes before getting back to work.")
else:
    print("We don't typically evaluate energy levels over 100 (or under 0), but if you're happy, please enjoy your day!")