#input() allows people to type in and enter something
import datetime
import calendar



username = input("Enter username")

if username == "Gabriel":
    print("Hello there, Gabriel!")



value = 12

if (value < 11):
    print("The value is less than 11")
else:
    print("The value is 11, or bigger than 11.")


current_time = datetime.datetime.current_time()
print("Time now: ", current_time)
#Let's get the current time
