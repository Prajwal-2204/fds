def In(element, list1):
    for item in list1:
        if element == item:
            return True
    return False

def first_appe(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            return i
    return -1

def revstr(string):
    revstr = ""
    for i in range(len(string)):
        revstr = string[i] + revstr
    return revstr

def str_count(string, char):
    count = 0
    for ch in string:
        if ch == char:
            count += 1
    return count

def max_len(splitL):
    max_length = 0
    longest_word = ""
    for word in splitL:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return max_length, longest_word

def is_palindrome(string):
    return string == string[::-1]

# Palindrome check
str1 = input("Enter string to check palindrome: ")
if is_palindrome(str1):
    print("The entered string is a palindrome")
else:
    print("The entered string is not a palindrome")

if revstr(str1) == str1:
    print("The entered string is a palindrome (using reverse string method)")
else:
    print("The entered string is not a palindrome (using reverse string method)")

# Maximum length word in a sentence
str2 = input("Enter the sentence to find the maximum length word: ")
words = str2.split()
max_length, longest_word = max_len(words)
print("Longest word length:", max_length, "Word:", longest_word)

# Character count in a string
str3 = input("Enter a string to check character count: ")
ch = input("Enter the character: ")
print("The count of the entered character is:", str_count(str3, ch))

# First appearance of a substring
str4 = input("Enter string to check first appearance of substring: ")
substring = input("Enter the substring: ")
index = first_appe(str4, substring)
if index != -1:
    print(substring, "is at index:", index)
else:
    print(substring, "is not found in the string")
