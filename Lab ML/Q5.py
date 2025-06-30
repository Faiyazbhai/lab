def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
text = input("Enter a string: ")
cleaned_text = text.replace(" ", "").lower()
if is_palindrome(cleaned_text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
