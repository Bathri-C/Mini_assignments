n=int(input("Enter the end value : "))
for num in range(1,n):
    if num%5==0 and num%3==0:
        print("Fizzbuzz")
    elif num%5==0:
        print("Buzz")
    elif num%3==0:
        print("Fizz")
    else:
        print(num)
