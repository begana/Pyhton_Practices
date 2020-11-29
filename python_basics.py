
first_name = input("What is your name? ")
print("hello,", first_name)
if first_name == 'Begana':
    print(first_name, "is learning Python.")
else:
    age = int(input("how old are you? "))
    if age <= 6:
        print("wow, you are {}! if you are confident with your reading already, you should learn Python.".format(age))
    else:
        print("you should totally learn Python, {}!".format(first_name))
    