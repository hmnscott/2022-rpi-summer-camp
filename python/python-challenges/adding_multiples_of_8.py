# adding multiples of 8 from 1 to 1000

sum = 0

for i in range(1, 1001):
    if i % 8 == 0:
        sum += i

print("")
print(f"The sum of multiples of 8 from 1 to 1000 is {sum}.")
print("")

print("Next, we'll add the multiples of 8 from 1 to N.")
N = input("What should N be? ")
N = int(N)

sum = 0

for i in range(1, N + 1):
    if i % 8 == 0:
        sum += i

print("")
print(f"The sum of multiples of 8 from 1 to {N} is {sum}.")
print("")