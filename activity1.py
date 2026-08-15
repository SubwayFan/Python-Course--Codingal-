flight_number = 9313
passenger = "Ryan Travis"
check_bag_default_cost = 40
number_of_bags = 1
#Researched five factors to determine ticket cost:
#base fare, taxes, airport fees, optional extras, and cost of checking bags
base_fare = 10
tax = 3.90
airport_fee = 1
optional_extra = 0
cost_of_checking_bags = check_bag_default_cost * number_of_bags
ticket_cost_1 = base_fare + tax + airport_fee + optional_extra + cost_of_checking_bags

print("Passenger", passenger, ", your total cost of the ticket is: " , ticket_cost_1)
print("Your flight number is", flight_number, ".")



flight_number = 8271
passenger = "Rochelle Linday"
check_bag_default_cost = 20
number_of_bags = 3
#Researched five factors to determine ticket cost:
#base fare, taxes, airport fees, optional extras, and cost of checking bags
base_fare = 5
tax = 5.19
airport_fee = 0.34
optional_extra = 3
cost_of_checking_bags = check_bag_default_cost * number_of_bags
ticket_cost_2 = base_fare + tax + airport_fee + optional_extra + cost_of_checking_bags

print("Passenger", passenger, ", your total cost of the ticket is: " , ticket_cost_2 )
print("Your flight number is", flight_number, ".")


if(ticket_cost_1 > ticket_cost_2):
    print("Ticket 1 is more expensive.")

else:
    print("Ticket 2 is more expensive.")

temp = 0
temp = ticket_cost_1
ticket_cost_1 = ticket_cost_2
ticket_cost_2 = temp

print("We have swapped the costs of the tickets.")
print("First ticket now costs: " , ticket_cost_1)
print("Second ticket now costs: " , ticket_cost_2)