#!/Users/frank.baileyaxonius.com/.pyenv/shims/python

# define function that takes 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} chesses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# call function and pass 20 and 30 as arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# create variables, then pass variables as arguments to cheese_and_crackers function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# passing sums as arguments to the function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


# combination of variables adding values and passing the results as arguments to the function
print("And we can combine the two, variables and math:")

cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

