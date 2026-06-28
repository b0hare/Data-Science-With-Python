# Write a function to return the sum of all numbers in a list.

def listSum(l):
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    return sum

list1 = [1,2,3,4,5,19,21]
print("\nList : ", list1)

print("Sum: ", listSum(list1), "\n")