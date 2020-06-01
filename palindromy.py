words_items = [
    "kajak",
    "potop"
]
def palindrome(items):  
    return items == items [::-1]
for item in words_items:
    print(palindrome(item))
