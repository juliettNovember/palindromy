def palindrome(sentence):
    """
    Return True if sentence is palindrom, otherwise False
    """
    return sentence == sentence[::-1]

words_items = [
    "kajak",
    "potop",
]

for item in words_items:
    print(palindrome(item))

