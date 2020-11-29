import math

def split_check(total, people):
    return math.ceil( total / people )

total_due = float(input("what is the total? $"))
number_of_people = int(input("how many people are you? "))
amount_due = split_check(total_due, number_of_people)
print("each person owes ${}".format(amount_due))