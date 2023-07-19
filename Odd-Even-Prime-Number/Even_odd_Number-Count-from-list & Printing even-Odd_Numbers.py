list1 = []     # Creating an empty list

n = int(input("Enter number of elements : "))
        # Talking n as number of elements as input

for i in range(0, n):   # iterating till the range
	ele = int(input())

	list1.append(ele)   # adding the element
print(list1)

even_count, odd_count = 0, 0
 
for num in list1:
    if num % 2 == 0:    # checking condition
        even_count += 1
    else:
        odd_count += 1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


for num in list1:
    if num % 2 == 0 :
        print("Even number in list", num )
    else:
        print("Odd Number in list.", num )