def is_palindrome(number):
    # Convert the number to a string for easy comparison
    num_str = str(number)
    # Compare the original number with its reverse
    return num_str == num_str[::-1]

num=int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
