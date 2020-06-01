import string
def palindrome(sentence):
    """
    Return True if sentence is palindrom, otherwise False
    """
    return sentence == sentence[::-1]

words_items = [
    "kajak",
    "potop",
    "Do geese see God?",
    "Że też łże jeż? łże też!"
]


for item in words_items:
    #item = item.replace(" ", "")
    item = item.translate(str.maketrans('', '', string.whitespace))
    item = item.translate(str.maketrans('', '', string.punctuation))
    item = item.lower()

    print(palindrome(item))
    

