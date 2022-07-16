# fizzbuzz
# FizzBuzz challenge: Print integers from 1 to N. 
# However, print "Fizz" if an integer is divisible by 3, 
# print "Buzz" if an integer is divisible by 5, 
# and print "FizzBuzz" if an integer is divisible by both 3 and 5.


print("")
N = int(input("What do you want to use for N? "))
print("")

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)