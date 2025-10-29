print ("Printing current and previous number sum in a range(10)")
the_range = range(10)
for number in the_range:
    previous_number = number - 1
    if previous_number < 0:
        previous_number = number
    the_sum = (number + previous_number)
    print("Current Number", number, "Previous Number", previous_number, "Sum: ", the_sum)