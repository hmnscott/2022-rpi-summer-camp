# add the integers from 1 to 1000

sum = 0

for i in range(1, 1001):
    sum = sum + i

print("")
print(f"The sum of the integers from 1 to 1000 is {sum}.")
print("")

# add the integers from 1 to N

sum = 0
print("Now let's add the numbers from 1 to N.")
N = input("What should N be: ")
N = int(N)

for i in range(1, N + 1):
    sum += i

print("")
print(f"The sum of the integers from 1 to {N} is {sum}.")
