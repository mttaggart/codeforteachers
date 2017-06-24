import sys # Import sys gives us access to command-line arguments

"""
Palindrome Detector

Detects palindromes from command-line input
"""

def is_pal(test):
    """
    Returns bool of whether test is a palindrome.
    Does so iteratively
    """
    # Reverse the test
    reverse_test = test[::-1]

    # Loop through to test test against reverse
    for i in range(len(test)):
        if test[i] != reverse_test[i]:
            return False

    return True


def is_pal_recur(test):
    # Check base cases
    # print(test)
    if len(test) == 1:
        return True

    if len(test) == 2:
        return test[0] == test[1]
   
    if test[0] == test[-1]:
        return is_pal_recur(test[1:-1])
    
    return False

string_to_test = sys.argv[1].replace(" ","").lower()

if is_pal_recur(string_to_test):
    print(string_to_test + " is a palindrome!")
else:
    print(string_to_test + " is NOT a palindrome!")