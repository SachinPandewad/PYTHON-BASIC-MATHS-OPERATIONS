# Printing Even Odd Numbers from list in range by user inputs.
# List = [a, b]

a = int(input("Enter Range Starts From Number."))
b = int(input("Enter Range Ends at Number."))
List=[a,b]
print("The Even Numbers in List are:")
for i in range (a, b+1):
    if i % 2 == 0:
        print(i)

print("The Odd Numbers in List are:")
for i in range (a, b):
    if (i % 2) != 0:
        print (i)