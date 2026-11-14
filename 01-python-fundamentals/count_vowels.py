s=input("Enter a string: ")
count=0
for char in s.lower():
    if char in 'aeiou':
        print(char)
        count+=1
print(f"Total number of vowels: {count}")