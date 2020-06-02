import string
def palindrome(sentence):
    """
    Return True if sentence is palindrom, otherwise False
    """
    sentence = sentence.translate(str.maketrans('', '', string.whitespace))
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    sentence = sentence.lower()
    return sentence == sentence[::-1]

words_items = [
    "kajak",
    "potop",
    "Do geese see God?",
    "Że też łże jeż? łże też!"
]
for item in words_items:
    print(palindrome(item))
    

