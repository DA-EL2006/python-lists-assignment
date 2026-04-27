a = [1, 2, 3]
b = a
b[0] = 100

print(a)
print(b)
print(id(a))
print(id(b))

#Why did both lists change? Because they are both equal to each other. It is the same list that is being printed as b = a
#Why are the ids the same? Because they are the same list in the memory of the computer.
#What does this mean? It means that when one list or variable is assigned to another variable, they both point to the same list in the memory as they are the same.