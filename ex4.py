#!/Users/frank.baileyaxonius.com/.pyenv/shims/python


#variable named car equals 100
cars = 100

# space_in_a_car variable equals 4.0
space_in_a_car = 4.0

# drivers variable equals 30
drivers = 30

# passengers variable = 90
passengers = 90

#cars_not_driven variable equals cars(100) minus drivers(30), which is 70
cars_not_driven = cars - drivers

#cars_driven variable equals whatever drivers equals (30)
cars_driven = drivers

#carpool_capacity variable equals total of cars_driven times space_in_a_car (120)
carpool_capacity = cars_driven * space_in_a_car

# average_passengers_per_car variable equals total of passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven


# for all lines below, print string, variable, then string
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

