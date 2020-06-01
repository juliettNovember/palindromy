#words = [
#    "kajak",
#    "potop"
#]
def palindrome(words):
    return words == words [::-1]

words = ["kajak"]
result = palindrome(words)

result = True 
print(result)