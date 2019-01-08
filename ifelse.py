print("How many classes have been held? ")
held = int(input())
print("How many of those have you attended? ")
attended = int(input())

attendance = attended/held
print("Do you have medical cause to sit in the exam? (y/n) ")
med = input()

print("Your attendance is: ", attendance)
if (med == "y" or med == "Y" or med == "yes") or attendance >= .75:
    print("You may sit in the exam.")
else:
    print("You may not sit in the exam.")
