def eve_or_odd(num):
    if num %2==0:
        return True
    return False

number = int(input("Enter a number: "))

if eve_or_odd(number):
    print(f"The {number} is even ")
else:
    print(f"The {number} is odd")
