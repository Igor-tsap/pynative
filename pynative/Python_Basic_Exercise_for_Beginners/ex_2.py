print ("Printing current and previous number sum in a range(10)")
previous_number = 0
for number in range(10):
    print("Current Number", number, "Previous Number", previous_number, "Sum: ", number + previous_number)
    previous_number = number