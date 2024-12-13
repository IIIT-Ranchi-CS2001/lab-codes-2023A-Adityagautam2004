def check_palindrome():
    user_input = input("Enter a string: ")
    user_input = user_input.strip()  
    user_input = user_input.lower() 
    if user_input == user_input[::-1]:
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")

check_palindrome()


