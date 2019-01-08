print("Input one: ")
one = input()

print("Input two: ")
two = input()

print("Input three: ")
three = input()

all = (one == two and two == three)
any = (one == two and two != three) or (one == three and one != two) or (one != two and two == three)
none = (one != two) and (two != three) and (one != three)

print ("All three values are equal: ", all)
print ("Two of the values are the same: ", any)
print ("None of the values are equal: ", none)
