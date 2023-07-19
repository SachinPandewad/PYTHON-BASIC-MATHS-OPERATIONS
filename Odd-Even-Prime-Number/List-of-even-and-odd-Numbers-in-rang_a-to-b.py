#printing EVEN and ODD list of numbers from youser input range bet a & b.

a = int(input(" Enter the number range start from. "))
b = int(input("Enter the number range end at. "))

print("Even Numbers in the list are")
for i in range (a,b):
    if i % 2 ==0:
        print(i)

print("Odd Numbers in the list are")
for i in range (a,b):
    if i %2 != 0:
        print(i)