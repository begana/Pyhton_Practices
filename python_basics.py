import math

def split_check(total, people):
    if people <= 1:
        raise ValueError("more than 1person is required")
    return math.ceil( total / people )

try:
    total_due = float(input("what is the total? $"))
    number_of_people = int(input("how many people are you? "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("oh no! that's not a valid value.")
    print("({})".format(err))
else:
    print("each person owes ${}".format(amount_due))