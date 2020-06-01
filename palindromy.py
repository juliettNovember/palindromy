words_items = [
    "kajak",
    "potop"
]
def palindrome(items):  
    """
    Prints result when words from list are palindromes
    Arguments:
    items from words_items
    """
    return items == items [::-1]
for item in words_items:
    print(palindrome(item))

