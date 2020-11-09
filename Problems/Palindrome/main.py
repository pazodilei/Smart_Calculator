word = input()
if word == ''.join([word[i] for i in range(len(word) - 1, -1, -1)]):
    print("Palindrome")
else:
    print("Not palindrome")
