# adding multiples of a from 1 to N

print("")
print("Let's add the multiples of a from 1 to N.")
a = int(input("a = "))
N = int(input("N = "))
print("")

sum = 0

for i in range(1, N + 1):
    if i % a == 0:
        sum += i

print(f"The sum of multiples of {a} from 1 to {N} is {sum}.")
print("")