while True:
    num = int(input("Enter Your number: "))
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
        
    else:
        print(num,"is not a prime number")
    
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break