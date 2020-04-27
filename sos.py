# Sum of Sequences
import math

fun = input("Enter the f(x) to be summed: ")
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
step = int(input("Enter the step to be shown: "))

def evalFunction(fun, num):
    x = num
    print("a" + str(num) + "[" + str(eval(fun)) + "]")
    return eval(fun)

def sumOfSequence(fun, lower, upper, step):
    total = 0
    count = 0
    for x in range(lower, upper + 1):
        total += evalFunction(fun, x)
        if x == lower + step * count:
            print("S" + str(x) + ": { " + str(total) + " }")
            count += 1
    print("End of the Summation~")

sumOfSequence(fun, lower, upper, step)
print("End of the Script~")